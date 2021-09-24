from django.urls import path
from .views import IndexView, ProductsView, ProductView

app_name = 'name_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:product_id>/', ProductView.as_view(), name='product')


]

