from  django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_slug,*args, **kwargs):
    print( f'slug: {menu_slug}')
    menu_items = MenuItem.objects.filter(slug = menu_slug)
    print(menu_items)
    return menu_items