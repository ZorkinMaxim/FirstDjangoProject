from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class TodoItem(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "High priority"),
        (PRIORITY_MEDIUM, "Medium priority"),
        (PRIORITY_LOW, "Low priority"),
    ]
    description = models.CharField(max_length=64)
    is_completed = models.BooleanField("Performed", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks")
    priority = models.IntegerField(
        "Priority", choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM
    )

    def __str__(self):
        return self.description.lower()

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("tasks:details", args=[self.pk])

    tags = TaggableManager()


class TagCount(models.Model):
    tag_slug = models.CharField(max_length=128)
    tag_name = models.CharField(max_length=128)
    tag_id = models.PositiveIntegerField(default=0)
    tag_count = models.PositiveIntegerField(db_index=True, default=0)
