import datetime
import os

from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    """
    @staticmethod
    """
    def entry_directory_path(self, filename):
        basename, extension = os.path.splitext(filename)
        name = str(datetime.datetime.now().time()).replace(':', '-').replace('.', '/')
        return 'files/{dir}/{basename}{ext}'.format(
            dir=str(datetime.datetime.now().date()),
            basename=name,
            ext=extension
        )

    title = models.CharField(max_length=512)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='placeholder.png', upload_to=entry_directory_path, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "base_entry"

    def save(self, *args, **kwargs):
        super(Entry, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1024 or img.width > 768:
            output_size = (1024, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)
