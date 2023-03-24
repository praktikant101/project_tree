from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True, blank=True, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.parent is None:
            return super().save(force_insert=True)
        if self.menu == self.parent.menu:
            super().save()


