from django.shortcuts import render
from .models import MenuItem

def start_page(request, url=None):
    return render(request, 'menu.html', {'menu_name': url})
