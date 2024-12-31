from django.urls import path
from .views import TopView, HomeView, LogoutView, LoginView


app_name = "app"

urlpatterns = [
    path("", TopView.as_view(), name="top"),
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
