from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    # def save(self, force_insert=False, force_update=False, using=None,
    #      update_fields=None):
    #      super().save()
    #
    #      img = Image.open(self.image.path)
    #      if img.height > 300 or img.width > 300:
    #          output_size = (300, 300)
    #          img.thumbnail(output_size)
    #          img.save(self.image.path)

# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)