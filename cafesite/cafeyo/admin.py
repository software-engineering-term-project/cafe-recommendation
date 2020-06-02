from django.contrib import admin

from .models import Gate, Category, Cafe, Menu
# Register your models here.


class MenuInline(admin.StackedInline):
    model = Menu
    extra = 1


class CafeAdmin(admin.ModelAdmin):
    inlines = [MenuInline]


admin.site.register(Gate)
admin.site.register(Category)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Menu)
