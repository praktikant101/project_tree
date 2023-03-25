from django.shortcuts import render
from django.views import View

from .models import Menu, Item


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


