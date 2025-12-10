from django.contrib import admin
from .models import Category, MenuItem, Ingredient, Recipe, Order, OrderItem, KitchenTicket

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available']
    list_filter = ['category', 'available']
    inlines = [RecipeInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'status', 'timestamp']
    list_filter = ['status']
    inlines = [OrderItemInline]

admin.site.register(Category)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Ingredient)
admin.site.register(Order, OrderAdmin)
admin.site.register(KitchenTicket)
