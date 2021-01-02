# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User, AbstractUser
# from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = False)
    username = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':1}))
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)
    years_in_academy = forms.CharField(required = False)
    class Meta:
        model = Profile
        fields = ['Gender','Role','years_in_academy','Profile_pic','cv']
