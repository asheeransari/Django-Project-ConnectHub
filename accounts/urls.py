from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path("home/", views.Home, name = "home"),
    # path("signup/", views.Signup, name = "signup"),
    # path("create_user/", views.Create_user, name = "create_user"),
    # path("login", views.Login, name = "login"),
    # path("logout/",views.Logout, name = "logout"),
    # path("profile/",views.Profile, name = "profile"),
    path("homev/", views.HomeView.as_view(), name = "homeView"),
    path("signupv/", views.SignupView.as_view(), name = "signupView"),
    path("", LoginView.as_view(
            template_name = "accounts/login.html"
        ), 
        name = "loginView"),
    path("logoutv/",LogoutView.as_view(), name = "logoutView"),
    path(
    "<int:pk>/profilev",
    views.ProfileView.as_view(),
    name="profileView"
    )
]
