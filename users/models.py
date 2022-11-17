from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='AwxR.png', upload_to='base/static/images')
    date_of_birth = models.DateField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
