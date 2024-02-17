from django.contrib import admin
from .models import Contact, Dish

class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'price', 'q', 'is_published', 'is_published_main', 'pub_date')
    search_fields = ('name', 'group')
    list_display_links = ('name', 'price')
    list_editable = ('is_published', 'is_published_main')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'second_name', 'email', 'phone', 'date')
    list_display_links = ('name', 'second_name')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Dish, DishAdmin)