import datetime
import os
import uuid

from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    def entry_directory_path(self, filename):
        basename, extension = os.path.splitext(filename)
        name = str(datetime.datetime.now().time()).replace(':', '-').replace('.', '/')
        return 'files/{dir}/{name}{ext}'.format(
            dir=str(datetime.datetime.now().date()),
            name=name + '-' + str(uuid.uuid4())[:8],
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

        image = Image.open(self.image.path)
        big_size = (1024, 768)

        if image.height > 1024 or image.width > 768:
            image.thumbnail(big_size)
            image.save(self.image.path)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Entry, self).delete(*args, **kwargs)
