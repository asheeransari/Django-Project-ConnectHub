from django.urls import path
from . import views

urlpatterns = [
    # path("createpost/", views.create_post, name="create_post"),

    # path(
    #     "like/<int:post_id>/",
    #     views.like_post,
    #     name="like_post"
    # ),

    # path(
    #     "comment/<int:post_id>/",
    #     views.add_comment,
    #     name="add_comment"
    # ),
    # path(
    # "edit/<int:post_id>/",
    # views.edit_post,
    # name="edit_post"
    # ),
    # path(
    # "delete/<int:post_id>/",
    # views.delete_post,
    # name="delete_post"
    # )

    path("create_post_v/", views.create_post_view.as_view(), name="create_post_View"),
    path(
    "<int:post_id>/like/",
    views.like_post_view.as_view(),
    name="like_post_View"
    ),
    path(
        "<int:post_id>/comment",
        views.add_comment_view.as_view(),
        name="add_comment_View"
    ),
    path(
        "<int:pk>/editv/",
        views.edit_post_view.as_view(),
        name="edit_post_View"
    ),
    path(
        "<int:pk>/deletev/",
        views.delete_post_view.as_view(),
        name="delete_post_View"
    )
]
