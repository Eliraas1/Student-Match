from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class TestPage(TemplateView):
    template_name = 'test.html'

class ThankPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

def Welcome_view(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'landing_page.html')
