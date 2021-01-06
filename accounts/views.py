from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, StudentSignUpForm, StudentUpdateForm
from .forms import UserUpdateForm,StudentSignUpForm, StudentUpdateForm, TeacherSignUpForm,TeacherUpdateForm
from . import forms
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Student,Teacher

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'templates/main.html', context)


# ===============================Student ===========================
def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(user= user)
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='studentg')
            user.groups.add(group)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_register.html', {'form': form})

@login_required
def student_profile(request,username):
    user1 = User.objects.get(username=username)
    context = {
        'user1': user1,
    }
    return render(request, 'accounts/student_profile.html', context)

@login_required
@allowed_users(allowed_roles = ['studentg'])
def edit_student(request):

    if request.method == 'POST':
        su_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if su_form.is_valid() and sp_form.is_valid():
            su_form.save()
            sp_form.save()
            messages.success(request, f'Your account has been updated!')
            return render(request,'accounts/student_profile.html')

    else:
        su_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'su_form': su_form,
        'sp_form': sp_form,
        'user1': request.user,
        }
    return render(request, 'accounts/edit_student.html', context)

# ===============================Teacher ===========================
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            teacher = Teacher.objects.create(user = user)
            # teacher.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='teacherg')
            user.groups.add(group)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = TeacherSignUpForm()
    return render(request, 'accounts/teacher_register.html', {'form': form})

@login_required
def teacher_profile(request,username):
    user1 = User.objects.get(username=username)
    context = {
            'user1': user1,
        }
    return render(request, 'accounts/teacher_profile.html', context)

@login_required
@allowed_users(allowed_roles = ['teacherg'])
def edit_teacher(request):

    if request.method == 'POST':
        tu_form = UserUpdateForm(request.POST, instance=request.user)
        tp_form = TeacherUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.teacher)
        if tu_form.is_valid() and tp_form.is_valid():
            tu_form.save()
            tp_form.save()
            messages.success(request, f'Your account has been updated!')
            return render(request, 'accounts/teacher_profile.html')
    else:
        tu_form = UserUpdateForm(instance=request.user)
        tp_form = TeacherUpdateForm(instance=request.user.teacher)

    context = {
        'tu_form': tu_form,
        'tp_form': tp_form,
        }
    return render(request, 'accounts/edit_teacher.html', context)

def profile(request,username):
    if request.user.student:
        return HttpResponse(student_profile(request, username))
    else:
        return HttpResponse(teacher_profile(request, username))
