from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from app.filters import TaskFilter
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from app.models import Task

from .forms import LoginForm, TaskForm


class TopView(TemplateView):
    template_name = "app/top.html"


class TaskFilterView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = "task_filter.html"
    filterset_class = TaskFilter

    # デフォルトの並び順を新しい順とする
    queryset = Task.objects.all().order_by('-pub_date')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


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
