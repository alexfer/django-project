from django.db import models
from django.utils import timezone


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "base_entry"
