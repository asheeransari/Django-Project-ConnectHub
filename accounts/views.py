from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate, logout
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import logging

logger = logging.getLogger(__name__)

# Create your views here.

# def Home(request):
#     posts = Post.objects.all().order_by("-created_at")
#     return render(request,"accounts/home.html",{"posts" : posts})

# def Signup(request):

#     form = SignupForm(request.POST or None)

#     return render(
#                 request,
#                 "accounts/signup.html",
#                 {"form" : form}
#             )
    
# def Create_user(request):

#     form = SignupForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Account created successfully. Please login.")
#             return redirect("login")
        
#     return render(
#         request,
#         "accounts/signup.html",
#         {"form": form}
#     )

# def Login(request):

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         if not username or not password:
#             messages.error(request, "Username and password are required.")
#             return redirect("login")

#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )

#         if user is not None:
#             login(request, user)
#             return redirect("home")

#         messages.error(request, "Invalid username or password.")

#     return render(request,"accounts/login.html")

# def Logout(request):
#     logout(request)
#     return redirect("login")

# @login_required
# def Profile(request):
#     return render(request,"accounts/profile.html")

class HomeView(ListView):
    template_name = "accounts/home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get(self, request, *args, **kwargs):
        logger.info(
            "Home page accessed by user_id=%s",
            request.user.id if request.user.is_authenticated else "anonymous"
        )

        return super().get(request, *args, **kwargs)

class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("loginView")

    def form_valid(self, form):
        user = form.save()

        logger.info(
            "New user registered: user_id=%s username=%s",
            user.id,
            user.username,
        )

        messages.success(
            self.request,
            "Account created successfully. Please login."
        )

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "accounts/profile.html"
    model = User
    context_object_name = "profile"

    def get(self, request, *args, **kwargs):
        logger.info(
            "Profile viewed: viewer_id=%s profile_id=%s",
            request.user.id,
            kwargs.get("pk"),
        )

        return super().get(request, *args, **kwargs)
    