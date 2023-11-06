from django.contrib import admin

from menu.models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Menu в админ-панели.
    """
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Конфигурация модели MenuItem в админ-панели.
    """
    list_display = ('pk', 'title', 'parent')
    list_filter = ('menu',)
    search_fields = ('title', 'slug')
    ordering = ('pk',)

    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
    )
