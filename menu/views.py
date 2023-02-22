from django.shortcuts import render
from .models import MainMenu, LastMenu, SecondMenu

def start_page(request):
    obj = MainMenu.objects.all()
    return render(request, 'menu.html', {'obj': obj})
