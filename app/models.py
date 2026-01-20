from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} needs {self.quantity_needed} {self.ingredient.unit} of {self.ingredient.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
        ('Cancelled', 'Cancelled'), 
    ]
    table_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Preparing')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - Table {self.table_number}"

    def get_order_items(self):
        return ", ".join([f"{item.quantity} x {item.menu_item.name}" for item in self.items.all()])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

class KitchenTicket(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    priority = models.IntegerField(default=5)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Ticket for Order {self.order.id}"
