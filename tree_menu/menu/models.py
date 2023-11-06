from django.db import models


class Menu(models.Model):
    """
    Модель меню, состоящего из множества пунктов, 
    образующих иерархическую структуру.
    """
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Заголовок меню'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name="Slug меню"
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    """
    Пункт меню, являющийся частью древовидной структуры. 
    Может иметь родительские и дочерние элементы.
    """
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок пункта меню'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name="Slug пункта меню"
    )
    description = models.TextField()

    menu = models.ForeignKey(
        Menu,
        blank=False,
        null=False,
        related_name='items',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def nest_level(self):
        if not self.parent:
            return 1
        return self.parent.nest_level() + 1

    def __str__(self) -> str:
        return self.title
