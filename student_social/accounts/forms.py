# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User, AbstractUser
# from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile,Student
from .models import Student, Teacher
from django.db import transaction

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

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     # profile_Pic = forms.ImageField(required = False)
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = False)
    username = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':1}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     cv = forms.FileField(required = False,label = 'CV')
#     Profile_pic = forms.ImageField(required = False)
#
#     class Meta:
#         model = Profile
#         fields = ['Gender','Role','years_in_academy','Profile_pic','cv']
#

# ==============================================Student =================================
class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField()
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        # Student.is_student = True
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class StudentUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)

    class Meta:
        model = Student
        fields = ['Role','Profile_pic','cv','study_choice','years_in_academy']

# ==============================================Teacher =================================

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField()
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.first_name = self.cleaned_data.get('first_name')
    #     user.last_name = self.cleaned_data.get('last_name')
    #     user.username = self.cleaned_data.get('username')
    #     user.email = self.cleaned_data.get('email')
    #     user.password1 = self.cleaned_data.get('password1')
    #     user.password2 = self.cleaned_data.get('password2')
    #     teacher = Teacher.objects.create(user=user)
    #     teacher.save()
    #     return user

class TeacherUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)
    class Meta:
        model = Teacher
        fields = ['undergraduate','description','Profile_pic','cv']
