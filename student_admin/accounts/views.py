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
            messages.success(request, f'Accout created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/login.html', {'form': form})

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
