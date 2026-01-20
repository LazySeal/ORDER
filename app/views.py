from django.shortcuts import render
from .models import MenuItem, Order


def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    items = MenuItem.objects.filter(available=True)
    return render(request, 'menu.html', {'items': items})

def order_list(request):
    orders = Order.objects.prefetch_related('items__menu_item').all().order_by('-timestamp')
    return render(request, 'orders.html', {'orders': orders})

