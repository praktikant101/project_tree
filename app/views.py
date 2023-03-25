from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Menu, Item
from django.template import Library

register = Library()


class MenuListView(View):

    def get(self, request):
        menus = Menu.objects.all()
        context = {
            "menus": menus
        }
        return render(request, "menu.html", context)


class MenuView(View):

    def get(self, request, pk):

        items = Item.objects.select_related('parent').prefetch_related('children').filter(menu_id=pk)

        context = {
            "items": items,
            "menu": items.first().menu.title
        }

        return render(request, "tree.html", context)


