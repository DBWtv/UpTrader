from  django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_slug,*args, **kwargs):
    if menu_slug == None:
        menu_items = MenuItem.objects.filter(parent = None)
    else:
        menu_items = MenuItem.objects.filter(slug = menu_slug)
    return menu_items