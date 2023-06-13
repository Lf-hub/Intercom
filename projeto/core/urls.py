from django.urls import path
from core.views import IndexView, CreateProduct

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateProduct.as_view(), name='create_product')

]