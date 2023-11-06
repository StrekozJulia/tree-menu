from django.shortcuts import render
from .models import Menu


def index(request, menu_slug=None, item_slug=None):
    template = 'menu/index.html'
    menus = Menu.objects.all()
    context = {
            'menus': menus,
            'current_menu': None,
            'current_item': None,
            'parent_tree': None
        }
    if menu_slug:
        current_menu = menus.get(slug=menu_slug)
        context['current_menu'] = current_menu
        if item_slug:
            current_item = current_menu.items.get(slug=item_slug)
            context['current_item'] = current_menu.items.get(slug=item_slug)
            
            child_item = current_item
            parent_tree = [current_item,]
            while child_item.parent:
                child_item = child_item.parent
                parent_tree.append(child_item)
            context['parent_tree'] = parent_tree

    return render(request, template, context)
