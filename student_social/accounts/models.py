from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='summaries')

RATE_CHOICES = [
	(1, '1 - Kill Him'),
	(2, '2 - Send to Hadas'),
	(3, '3 - Good'),
	(4, '4 - Very Good'),
	(5, '5 - Perfect')
]


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
    admin_rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES,default=0)
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

class Rating(models.Model):
	source = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)
	def __str__(self):
		return self.source

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
    rating = models.ManyToManyField(Rating, blank = True)
    admin_rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES,default=0)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_pic.path)

# ============================================================================

class Report(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=3000, blank=True)
	rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
	# likes = models.PositiveIntegerField(default=0)
	# unlikes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.user.username
