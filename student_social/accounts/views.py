from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from . import forms
# from .form import UserCreateForm, register_extra
# from .models import regiter_extra_model,User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             usename = form.cleaned_data.get('username')
#             messages.success(request, f'Accout created for {username}.')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request,'accounts/login.html', {'form': form})
#
# # Create your views here.
# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

# def profile(request):
#     if request.method == 'POST':
#         uform = UserUpdateForm(request.POST, instance=request.user)
#         pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#
#         if uform.is_valid() and pform.is_valid():
#             uform.save()
#             pform.save()
#             messages.success(request, f'Account has been updated.')
#             return redirect('profile')
#     else:
#         uform = UserUpdateForm(instance=request.user)
#         pform = ProfileUpdateForm(instance=request.user.profile)
#
#     return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})

#
# def register(request):
#     if request.user.is_authenticated:
#         return redirect("stundet_admin:index")
#     else:
#         if request.method == "POST":
#             form = UserCreateForm(request.POST or None)
#             form1 = register_extra(request.POST or None)
#             if form.is_valid() and form1.is_valid():
#                 user = form.save()
#                 profile = form1.save(commit=False)
#                 profile.user = user
#
#                 if 'image' in request.FILES:
#                     profile.image=request.FILES['image']
#                 profile.save()
#
#                 user1 = form1.save()
#                 username = form.cleaned_data['username']
#                 raw_password = form.cleaned_data.get('password1')
#
#                 user = authenticate(username=user.username, password=raw_password)
#
#                 login(request, user)
#
#                 return redirect("student_admin:index")
#         else:
#             form = RegistrationForm()
#             form1 = register_extra()
#         return render(request, "accounts/signup.html", {"form": form, "form1": form1})
#
#
# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect("student_admin:index")
#     else:
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("student_admin:index")
#                 else:
#                     return render(request, 'accounts/login.html', {"error": "your account has been disabled."})
#             else:
#                 return render(request, 'accounts/login.html', {"error": "invalid Username or Password.try again."})
#         return render(request, 'accounts/login.html')
#
#
# def logout_user(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect("accounts:login")
#     else:
#         return redirect("accounts:login")
