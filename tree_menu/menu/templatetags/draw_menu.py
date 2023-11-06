from django import template

register = template.Library()


@register.inclusion_tag('menu/menu_items.html', takes_context=True)
def draw_menu(context, parent):
    menu = context['menu']
    children = menu.items.filter(parent=parent)
    result = {
        'children': children,
        'current_item': context['current_item'],
        'menu': context['menu'],
        'parent_tree': context['parent_tree']
    }
    return result
