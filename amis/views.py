from django.shortcuts import render
from property.models import Property


def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def faq(request):
    return render(request, 'faq.html', {})
