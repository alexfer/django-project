from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from content.models import Entry


class Comment(models.Model):
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'base_comment'
