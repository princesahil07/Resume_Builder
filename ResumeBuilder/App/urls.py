from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("resume_info/", views.resume_info, name="resume_info"),
    path("logout_user/", views.logout_user, name="logout_user")
]