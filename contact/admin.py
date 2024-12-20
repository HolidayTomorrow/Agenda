from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email',
    ordering = 'id',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20
    list_max_show_all = 80
    list_display_links = 'id', 'first_name', 'email',
    
    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',