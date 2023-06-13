from django.contrib import admin
from core.models import ProductModel, StockModel, StockLineModel

# Register your models here.

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price')


@admin.register(StockModel)
class StockAdmin(admin.ModelAdmin):
    list_display = ('employee', 'invoice')


@admin.register(StockLineModel)
class StockLineAdmin(admin.ModelAdmin):
    list_display = ('stock', 'product', 'amount', 'balance')