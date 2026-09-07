from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Images
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Likes, Comments
from django.contrib.contenttypes.models import ContentType
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import logging
from accounts.performance import log_performance
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)

# Create your views here.

# @login_required
# def create_post(request):
#     form = PostForm(request.POST or None, request.FILES or None)

#     if form.is_valid():

#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()

#         image = request.FILES.get("image")

#         if image:
#             Images.objects.create(
#                 author=request.user,
#                 image=image,
#                 content_object=post
#             )

#         return redirect("home")

#     return render(
#         request,
#         "posts/create_post.html",
#         {"form": form}
#     )

@method_decorator(log_performance("Create Post"), name="dispatch")
class create_post_view(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("homeView")

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user

            response = super().form_valid(form)

            image = self.request.FILES.get("image")

            if image:
                Images.objects.create(
                    author=self.request.user,
                    image=image,
                    content_object=self.object
                )

                logger.info(
                    "Post created with image: post_id=%s user_id=%s",
                    self.object.id,
                    self.request.user.id
                )
            else:
                logger.info(
                    "Post created: post_id=%s user_id=%s",
                    self.object.id,
                    self.request.user.id
                )

            return response

        except Exception:
            logger.exception(
                "Error while creating post: user_id=%s",
                self.request.user.id
            )
            raise

# @login_required
# def like_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     content_type = ContentType.objects.get_for_model(Post)

#     like = Likes.objects.filter(
#         author=request.user,
#         content_type=content_type,
#         object_id=post.id
#     ).first()

#     if like:
#         like.delete()
#     else:
#         Likes.objects.create(
#             author=request.user,
#             content_type=content_type,
#             object_id=post.id
#         )

#     return redirect("home")

# async def like_post(request, post_id):

#     user = await request.auser()

#     if not user.is_authenticated:
#         return redirect("loginView")

#     try:
#         post = await Post.objects.aget(id=post_id)
#     except Post.DoesNotExist:
#         return redirect("homeView")

#     content_type = await ContentType.objects.aget(
#         app_label="posts",
#         model="post"
#     )

#     like = await Likes.objects.filter(
#         author=user,
#         content_type=content_type,
#         object_id=post.id
#     ).afirst()

#     if like:
#         await like.adelete()
#     else:
#         await Likes.objects.acreate(
#             author=user,
#             content_type=content_type,
#             object_id=post.id
#         )

#     return redirect("homeView")

@method_decorator(log_performance("Like Post"), name="dispatch")
class like_post_view(LoginRequiredMixin, View):

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        content_type = ContentType.objects.get_for_model(Post)

        like = Likes.objects.filter(
            author=request.user,
            content_type=content_type,
            object_id=post.id
        ).first()

        if like:
            like.delete()

            logger.info(
                "Post unliked: user_id=%s post_id=%s",
                request.user.id,
                post.id,
            )

        else:
            Likes.objects.create(
                author=request.user,
                content_type=content_type,
                object_id=post.id
            )

            logger.info(
                "Post liked: user_id=%s post_id=%s",
                request.user.id,
                post.id,
            )

        return redirect(f"/homev/#like-{post.id}")

@method_decorator(log_performance("Comment Post"), name="dispatch")
class add_comment_view(LoginRequiredMixin, View):

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        text = request.POST.get("text")

        if text:
            content_type = ContentType.objects.get_for_model(Post)

            Comments.objects.create(
                author=request.user,
                text=text,
                content_type=content_type,
                object_id=post.id
            )

            logger.info(
                "Comment added: user_id=%s post_id=%s",
                request.user.id,
                post.id,
            )

        else:
            logger.warning(
                "Empty comment submission: user_id=%s post_id=%s",
                request.user.id,
                post.id,
            )

        return redirect(f"/homev/#comment-{post.id}")

# @login_required
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     text = request.POST.get("text")

#     if text:
#         content_type = ContentType.objects.get_for_model(Post)

#         Comments.objects.create(
#             author=request.user,
#             text=text,
#             content_type=content_type,
#             object_id=post.id
#         )

#     return redirect("home")

# async def add_comment(request, post_id):

#     user = await request.auser()

#     if not user.is_authenticated:
#         return redirect("loginView")

#     try:
#         post = await Post.objects.aget(id=post_id)
#     except Post.DoesNotExist:
#         return redirect("home")

#     text = request.POST.get("text")

#     if text:
#         content_type = await ContentType.objects.aget(
#             app_label="posts",
#             model="post"
#         )

#         await Comments.objects.acreate(
#             author=user,
#             text=text,
#             content_type=content_type,
#             object_id=post.id
#         )

#     return redirect("homeView")

# @login_required
# def edit_post(request, post_id):

#     post = get_object_or_404(
#         Post,
#         id=post_id,
#         author=request.user
#     )

#     form = PostForm(
#         request.POST or None,
#         instance=post
#     )

#     if form.is_valid():
#         form.save()
#         return redirect("home")

#     return render(
#         request,
#         "posts/edit_post.html",
#         {"form": form, "post": post}
#     )

class edit_post_view(LoginRequiredMixin, UpdateView):
    template_name = "posts/edit_post.html"
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("homeView")

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        )

    def form_valid(self, form):
        response = super().form_valid(form)

        logger.info(
            "Post updated: post_id=%s user_id=%s",
            self.object.id,
            self.request.user.id,
        )

        return response

# @login_required
# def delete_post(request, post_id):

#     post = get_object_or_404(
#         Post,
#         id=post_id,
#         author=request.user
#     )

#     if request.method == "POST":
#         post.delete()
#         return redirect("home")

#     return render(
#         request,
#         "posts/delete_post.html",
#         {"post": post}
#     )

class delete_post_view(LoginRequiredMixin, DeleteView):
    template_name = "posts/delete_post.html"
    model = Post
    success_url = reverse_lazy("homeView")

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        )

    def form_valid(self, form):
        post_id = self.object.id
        user_id = self.request.user.id

        response = super().form_valid(form)

        logger.info(
            "Post deleted: post_id=%s user_id=%s",
            post_id,
            user_id,
        )

        return response