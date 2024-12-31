from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms


class TopView(TemplateView):
    template_name = "app/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "app/home.html"

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "app/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "app/login.html"
