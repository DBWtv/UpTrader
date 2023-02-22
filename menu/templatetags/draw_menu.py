from  django import template
from ..models import MainMenu

register = template.Library()

@register.simple_tag
def draw_menu(obj):
    return MainMenu.get_absolute_url(obj)