from django.contrib import admin
from .models import category, Unit, Item, Supplier, Order, Employee

# Register your models here.
admin.site.register(category)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Employee)