from django.db import models

from taggit.managers import TaggableManager
from base.models import BaseModel


class MenuCategory(BaseModel):
    category = models.CharField(
        max_length=200
    )
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.category

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Category"
        db_table = "menu_category"


class Menu(BaseModel):
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.RESTRICT,
        related_name='menus'
    )
    name = models.CharField(
        max_length=200,
    )
    link = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        db_table = 'menu'
