import logging
from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from app.filters import TaskFilter
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from app.models import Task
from app.tables import TaskTable

from .forms import LoginForm, TaskForm

import django_otp
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.qr import write_qrcode_image

logger = logging.getLogger(__name__)

class TopView(TemplateView):
    template_name = "app/top.html"


class TaskFilterView(LoginRequiredMixin, FilterView, SingleTableView, View):
    model = Task
    table_class = TaskTable
    template_name = "task_filter.html"
    filterset_class = TaskFilter

    # デフォルトの並び順を新しい順とする
    queryset = Task.objects.all().order_by('-pub_date')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 100

    def get(self, request, *args, **kwargs):
        if not request.user.is_verified():
            logger.warning("OTP 未検証")
            return redirect("app:verify_otp")

        logger.info("OTP 検証済み")
        return super().get(request, **kwargs)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # マークダウンをHTMLに変換してテンプレートに渡す
        context['description_html'] = self.object.render_notes_as_html()
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('app:home')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('app:home')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('app:home')


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "app/login.html"


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "app/login.html"


# class TaskView():
#     def new(request):
#         if request.method == "POST":
#             form = TaskForm(request.POST)
#             if form.is_valid():
#                 task = Task()
#                 task.name = form.cleaned_data["name"]
#                 task.status = False
#                 task.pub_date = datetime.now()
#                 task.notes = form.cleaned_data["notes"]
#                 task.save()
#                 return redirect(reverse('app:home'))
#             else:
#                 raise Exception("hogehoge")
#         else:
#             form = TaskForm()
#             return render(request, "app/new-task.html", {"form": form})

#     def update(request):
#         if request.method == "PUT":
#             ...
#         else:
#             form = TaskForm()
#             task_id = form.cleaned_data["id"]
#             return render(request, "app/update-task.html", {"task": task})

class OtpView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/otp.html")

    def post(self, request, *args, **kwargs):
        # デバイスを追加する。
        device = TOTPDevice.objects.create(user=request.user, name='default', confirmed=False)

        # write_qrcode_image を使うことで、QRコードを生成できる。
        response = HttpResponse(content_type='image/svg+xml')
        write_qrcode_image(device.config_url, response)

        return response


# トークンを検証する。
class VerifyOtpView(LoginRequiredMixin, View):
    def get_otp_device(self, user):
        return TOTPDevice.objects.filter(user=user).first()

    def get(self, request, *args, **kwargs):
        otp_device = self.get_otp_device(request.user)
        if otp_device is None:
            logger.warning("OTP デバイスなし")
            return redirect("app:otp")
        return render(request, "app/verify_otp.html")

    def post(self, request, *args, **kwargs):
        otp_device = self.get_otp_device(request.user)
        if otp_device is None:
            logger.warning("OTP デバイスなし")
            return redirect("app:otp")

        if otp_device.verify_token(request.POST.get('otp_token')):
            otp_device.confirmed = True
            otp_device.save()
            django_otp.login(request, otp_device)
            logger.info("OTP 認証成功")
            return redirect("app:home")

        logger.error("OTP が違います")
        return redirect("app:verify_otp")
