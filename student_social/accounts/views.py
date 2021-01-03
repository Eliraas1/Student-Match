from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, StudentSignUpForm, StudentUpdateForm
from .forms import UserUpdateForm,StudentSignUpForm, StudentUpdateForm, TeacherSignUpForm,TeacherUpdateForm
from . import forms

#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/signup.html', {'form': form})
#
#
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')
#
# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return render(request, 'accounts/profile.html')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#         }
#     return render(request, 'accounts/edit_profile.html', context)
#

# ===============================Student ===========================
def student_register(request):

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student_group')
            user.groups.add(group)

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_register.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['student_group'])
def student_profile(request):
    return render(request, 'accounts/student_profile.html')

@login_required
@allowed_users(allowed_roles=['student_group'])
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
            return render(request, 'accounts/student_profile.html')

    else:
        su_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'su_form': su_form,
        'sp_form': sp_form,
        }
    return render(request, 'accounts/edit_student.html', context)

# ===============================Teacher ===========================
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='teacher_group')
            user.groups.add(group)

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = TeacherSignUpForm()
    return render(request, 'accounts/teacher_register.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['teacher_group'])
def teacher_profile(request):
    return render(request, 'accounts/teacher_profile.html')

@login_required
@allowed_users(allowed_roles=['teacher_group'])
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
