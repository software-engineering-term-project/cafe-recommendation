from django.contrib import admin

from .models import Gate, Category, Cafe, Menu
# Register your models here.
admin.site.register(Gate)
admin.site.register(Category)
admin.site.register(Cafe)
admin.site.register(Menu)
