from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, AbstractUser

class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Adress"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']




    # class Meta:
    #     fields = ('username','email','password1','password2')
    #     model = get_user_model()
    #
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].label = 'Display Name'
    #     self.fields['email'].label = "Email Adress"

# class CustomUser(AbstractUser):
#     type_choices = (
#         ('SU', 'Admin'),
#         ('A', 'Student'),
#         ('B', 'Teacher'),
#     )
#     user_type = models.CharField(max_length=2,
#                                  choices=type_choices,
#                                  default='B')
#
# class UserDetails(model.Model):
#     type = models.OneToOneField('CustomUser')
#     extra_info = models.CharField(max_length=200)
