from django.contrib import admin
from menu.models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)