from django.db.models import Prefetch
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
        menu = Menu.objects.prefetch_related(Prefetch("items",
                                                       queryset=Item.objects.filter(parent_id=None))).get(id=pk)
        items = Item.objects.select_related('parent').prefetch_related('children').filter(pk=pk)
        context = {
            "items": items,
        }

        return render(request, "menu_view.html", context)
