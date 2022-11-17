from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "base_entry"
