from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']




# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].label = 'Display Name'
#         self.fields['email'].label = "Email Adress"
#         self.fields['Profile_Pic'].label = "Profile Picture"

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = False)
    username = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':1}))
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)
    # years_in_academy = forms.CharField(blank = True)
    # is_student = forms.BooleanField(required = True)

    class Meta:
        model = Profile
        fields = ['image','Gender','description','Role','cv','years_in_academy']

    # def __init__(self,*args,**kwargs):
    #     super(ProfileUpdateForm,self).__init__(*args,**kwargs)
    #     if self.fields['is_student']:
    #         print('True')
    #         self.fields +=
