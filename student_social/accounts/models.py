from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='summaries')
#
# class Profile(models.Model):
#
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     Profile_pic = models.ImageField(default='default.gif',upload_to='profile_pic')
#     description = models.TextField(null=True, blank=True)
#     gender = (('male', "Male"), ('female', "Famale"))
#     Gender = models.CharField(choices=gender, max_length=300,null=True)
#     role = (('student', "Student"), ('teacher', 'Teacher'))
#     Role = models.CharField(choices=role, max_length=300,null=True)
#     cv = models.FileField(upload_to='cv', blank=True)
#     # summaries = models.ManyToManyField('File')
#     STUDY_CHOICE = (('aerospace engineering','Aerospace Engineering'),('architecture','Architecture'),('business','Business'),('chemical engineering','Chemical Engineering'),('civil engineering','Civil Engineering'),('computer engineering','Computer Engineering'),('computer science','Computer Science'),('economics','Economics'),('education','Education'),
#     ('electrical engineering','Electrical Engineering'),('engineering','Engineering'),('graphic design','Graphic Design'),('industrial engineering','Industrial Engineering'),('software engineering','Software Engineering'))
#     study_choice = study_choice = models.CharField(choices = STUDY_CHOICE, max_length = 300, null=True ,blank = False)
#     YEAR_IN_SCHOOL_CHOICES = (
#         ('FR', 'Freshman'),
#         ('SO', 'Sophomore'),
#         ('JR', 'Junior'),
#         ('SR', 'Senior'),
#         ('GR', 'Graduate'),
#         )
#     years_in_academy = models.CharField(choices = YEAR_IN_SCHOOL_CHOICES, max_length = 300, null=True ,blank = False)
#
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
#
#     def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)
#
#         img = Image.open(self.Profile_pic.path)
#
#         if img.height > 300 or img.width > 300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

#
# class User(AbstractUser, PermissionsMixin):
#     is_Student = models.BooleanField(default=False)
#     is_Teacher = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()


# =================================== Student =================================
class Student(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE,primary_key=True)
    role = (('student', "Student"), ('teacher', 'Teacher'))
    Role = models.CharField(choices=role,default=1, max_length=300,null=True)
    Profile_pic = models.ImageField(default='default.gif',upload_to='profile_pic')
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = models.CharField(choices=gender, max_length=300,null=True)
    location = models.CharField(max_length=20)
    STUDY_CHOICE = (('aerospace engineering','Aerospace Engineering'),('architecture','Architecture'),('business','Business'),('chemical engineering','Chemical Engineering'),('civil engineering','Civil Engineering'),('computer engineering','Computer Engineering'),('computer science','Computer Science'),('economics','Economics'),('education','Education'),
    ('electrical engineering','Electrical Engineering'),('engineering','Engineering'),('graphic design','Graphic Design'),('industrial engineering','Industrial Engineering'),('software engineering','Software Engineering'))
    study_choice = models.CharField(choices = STUDY_CHOICE, max_length = 300, null=True ,blank = False)
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
        )
    years_in_academy = models.CharField(choices = YEAR_IN_SCHOOL_CHOICES, max_length = 300, null=True ,blank = False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_pic.path)

# =================================== Teacher =================================
class Teacher(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    is_student = models.BooleanField(default=False)
    role = (('student', "Student"), ('teacher', 'Teacher'))
    Role = models.CharField(choices=role,default = 0, max_length=300,null=True,blank = False)
    Profile_pic = models.ImageField(default='default2.jpg',upload_to='profile_pic')
    description = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='cv')
    UNDERGRADUATE = (
        ('BA', 'Bachelor'),
        ('BSc', 'Bachelor of Science'),
        ('MA', 'Master'),
        ('MSc', 'Master of Science'),
        ('PhD', 'Doctor of Philosophy'),
        )
    undergraduate = models.CharField(choices = UNDERGRADUATE, max_length = 300, null=True ,blank = False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_pic.path)
