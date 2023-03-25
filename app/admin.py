from django.contrib import admin, messages

from .models import Menu, Item


class ItemAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if request.POST["parent"] == "":
            return super(ItemAdmin, self).save_model(request, obj, form, change)

        if not obj.menu == obj.parent.menu:
            messages.set_level(request, messages.ERROR)
            messages.add_message(request, messages.ERROR, f"Invalid menu: item's menu must be same as its parents "
                                                          f"({obj.parent.menu.title})")
        super(ItemAdmin, self).save_model(request, obj, form, change)


class ItemInline(admin.TabularInline):
    model = Item


class MenuAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
