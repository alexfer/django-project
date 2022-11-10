from django.db import models
from django.utils import timezone
from content.models import Entry


# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'base_comment'
