from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserCreateForm

from . import forms

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usename = form.cleaned_data.get('username')
            messages.success(request, f'Accout created for {username}.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/login.html', {'form': form})

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

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
