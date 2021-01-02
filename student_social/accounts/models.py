from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Profile_pic = models.ImageField(default='default.gif',upload_to='profile_pic')
    description = models.TextField(null=True, blank=True)
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = models.CharField(choices=gender, max_length=300,null=True)
    role = (('student', "Student"), ('teacher', 'Teacher'))
    Role = models.CharField(choices=role, max_length=300,null=True)
    cv = models.FileField(upload_to='files')
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
        )
    years_in_academy = models.CharField(choices = YEAR_IN_SCHOOL_CHOICES, max_length = 300, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    # def save(self):
    #     super().save()
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

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
