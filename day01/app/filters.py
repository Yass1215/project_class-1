import django_filters
from .models import category, Item

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = category
        fields = '__all__'

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['name', 'category', 'unit']        