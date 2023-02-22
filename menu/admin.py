from django.contrib import admin
from .models import MainMenu, SecondMenu, LastMenu

admin.site.register([MainMenu, SecondMenu, LastMenu])
