from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'preview', 'name', 'qty', 'popular', 'new', 'sale_percent']
    list_editable = ['popular', 'new', 'sale_percent']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['id', 'preview', 'name']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.main_image.url}" style="height: 128px; width: 128px">')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'region', 'city', 'price', 'status', 'date_created', 'date_updated']
    list_editable = ['status']
    list_display_links = ['id', 'name', 'phone']
    list_filter = ['name', 'phone', 'status', 'city', 'region', 'date_created', 'date_updated']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
