from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, AbstractUser
from .models import Profile

# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField()
#     Profile_Pic = forms.ImageField(required=False)
#     class Meta:
#         model = User
#         fields= ['username','email','password1','password2','Profile_Pic']
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].label = 'Display Name'
#         self.fields['email'].label = "Email Adress"
#         self.fields['Profile_Pic'].label = "Profile Picture"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


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
