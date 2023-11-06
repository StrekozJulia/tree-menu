from django.shortcuts import render
from .models import Menu


def index(request, menu_slug=None, item_slug=None):
    template = 'menu/index.html'
    menus = Menu.objects.all()
    context = {
            'menus': menus,
            'current_menu': None,
            'current_item': None,
        }
    if menu_slug:
        current_menu = menus.get(slug=menu_slug)
        context['current_menu'] = current_menu
        if item_slug:
            context['current_item'] = current_menu.items.get(slug=item_slug)

    return render(request, template, context)
