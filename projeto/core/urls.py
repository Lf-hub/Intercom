from django.urls import path
from core.views import IndexView,\
    CreateProduct,\
    UpdateProductView,\
    DetailProductView,\
    DeleteProductView,\
    SaleProduct

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateProduct.as_view(), name='create_product'),
    path('detail/<int:pk>/', DetailProductView.as_view(), name='detail_product'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    path('sale/', SaleProduct.as_view(), name='sale_product'),
]