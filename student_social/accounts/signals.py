from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from .models import User
from django.dispatch import receiver
# from .models import Profile,Student
from .models import Student,Teacher
from django.contrib.auth.models import Group
# signal that gets fired after the user is saved

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

# ========================= student ======================

@receiver(post_save, sender=User)
def create_Student(sender, instance, created, **kwargs):
    print(sender)
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_Student(sender, instance, **kwargs):
    instance.student.save()


# ========================= teacher ======================

@receiver(post_save, sender=User)
def create_teacher(sender, instance, created, **kwargs):
    print(sender)
    if created:
        Teacher.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_teacher(sender, instance, **kwargs):
    instance.teacher.save()

# @receiver(post_save, sender=Student)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#
#     """
#     sender: sender model from which you'll receive signal from
#     instance: model instance(record) which is saved (it will be instance of sender model)
#     """
#     # teacher = Teacher.objects.create(user=instance)
#     if created:
#         # if request.user.groups.all.0.name == 'teacher_group'
#           # used to perform action only at creation time (avoid the code to execute during any update)
#         group = Group.objects.get(name = group_name)
#         print("created")
#         if group in user.groups.all():  # access the field of instance
#             print("vagina amak")
#             student = Student.objects.create(user=instance) # you have correctly passed instance to foreign key and you just need to check condition for the same
#         #
#         else:
#             print("vagina amak")
#             teacher = Teacher.objects.create(user=instance)



#
# @receiver(post_save, sender=User)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()
# @receiver(post_save, sender=User)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()
