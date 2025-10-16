from autoslug import AutoSlugField

from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from taggit.managers import TaggableManager

from core_apps.common.models import TimeStampedModel, ContentView
from core_apps.profiles.models import Profile


User = get_user_model()


class Post(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )

    slug = AutoSlugField(
        verbose_name=_("Slug"),
        populate_from="title",
        unique=True,
    )

    body = models.TextField(verbose_name=_("Post"))
    tags = TaggableManager(verbose_name=_("Tags"))

    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name="posts"
    )

    bookmarked_by = models.ManyToManyField(
        User,
        verbose_name=_("Bookmarked by"),
        related_name="bookmarked_posts",
        blank=True
    )

    upvotes = models.PositiveIntegerField(
        verbose_name=_("Upvotes"),
        default=0
    )

    upvoted_by = models.ManyToManyField(
        User,
        verbose_name=_("Upvoted by"),
        related_name="upvoted_posts",
        blank=True
    )

    downvotes = models.PositiveIntegerField(
        verbose_name=_("Downvotes"),
        default=0
    )

    downvoted_by = models.ManyToManyField(
        User,
        verbose_name=_("Downvoted by"),
        related_name="downvoted_posts",
        blank=True
    )

    content_views = GenericRelation(
        # The generic relation allows to create a reverse relationship from the post model to the content view model
        # It enables to access the content views associated with a specific post using the related querry name, which is post

        # Example:
        # If we have Post instance called post, we can access the content views using post.content_views.all()
        # This will return a queryset of the content view instances related to that specific post
        ContentView,
        related_query_name="content_viewed_posts"
    )


    def __str__(self) -> str:
        return f"{self.title}"


    @classmethod
    def get_popular_tags(cls, limit=5):
        """
            This method is goind to retrieve the most popular tags associated with the posts in the post model.
        """
        return cls.tags.annotate(
            post_count=Count("taggit_taggeditem_items")
        ).order_by("-post_count")[:limit]


    def save(self, *args, **kwargs) -> None:
        if not (
            self.author.is_superuser or self.author.is_staff or self.author.profile.occupation == Profile.OccupationChoices.Tenant
        ):
            raise ValueError("Only tenants, superusers or staff members can create posts.")

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Reply(TimeStampedModel):
    post = models.ForeignKey(
        Post,
        verbose_name=_("Post"),
        on_delete=models.CASCADE,
        related_name="replies"
    )

    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name="replies"
    )

    body = models.TextField(verbose_name=_("Reply"))


    def __str__(self) -> str:
        return f"Reply by {self.author.username} on {self.post.title}"


    class Meta:
        verbose_name = _("Reply")
        verbose_name_plural = _("Replies")
