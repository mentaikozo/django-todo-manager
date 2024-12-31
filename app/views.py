from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from app.models import Task

from .forms import LoginForm, TaskForm


class TopView(TemplateView):
    template_name = "app/top.html"


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "app/login.html"


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "app/login.html"


class TaskView():
    def new(request):
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = Task()
                task.name = form.cleaned_data["name"]
                task.status = False
                task.pub_date = datetime.now()
                task.notes = form.cleaned_data["notes"]
                task.save()
                return redirect(reverse('app:home'))
            else:
                raise Exception("hogehoge")
        else:
            form = TaskForm()
            return render(request, "app/new-task.html", {"form": form})

