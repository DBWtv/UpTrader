from django.shortcuts import render
from .models import MainMenu, LastMenu, SecondMenu

def start_page(request):
    return render(request, 'menu.html')
