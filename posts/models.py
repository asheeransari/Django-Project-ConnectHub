from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Images(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="user_img/"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

class Likes(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "content_type", "object_id"],
                name="unique_user_like"
            )
        ]

class Comments(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField(max_length=300)

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=100)
    images = GenericRelation(
        Images,
        related_query_name="post"
    )
    comments = GenericRelation(Comments)
    likes = GenericRelation(Likes)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)