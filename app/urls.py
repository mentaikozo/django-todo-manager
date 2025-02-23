from django.urls import path
from .views import TopView, LogoutView, LoginView, OtpView, VerifyOtpView, TaskFilterView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView


app_name = "app"

urlpatterns = [
    path("", TopView.as_view(), name="top"),
    path("home/", TaskFilterView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("otp/", OtpView.as_view(), name="otp"),
    path("verify_otp/", VerifyOtpView.as_view(), name="verify_otp"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", TaskDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete"),
]
