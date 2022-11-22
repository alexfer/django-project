import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):

    def profile_directory_path(self, filename):
        basename, extension = os.path.splitext(filename)
        return 'profile/{id}/{basename}{ext}'.format(id=self.user.id, basename=str(uuid.uuid4())[:8], ext=extension)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile.png', upload_to=profile_directory_path, null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
