from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}'



# from store.wsgi import *
# from users.models import User




