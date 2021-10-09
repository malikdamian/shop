from django.urls import path
from .views import IndexView, ProductsView, ProductView, AddProductView, EditProductView, DeleteProductView, \
    CheckoutView, CartView, update_item

app_name = 'name_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:product_id>/', ProductView.as_view(), name='product'),
    path('add-product/', AddProductView.as_view(), name='add-product'),
    path('edit-product/<int:product_id>/', EditProductView.as_view(), name='edit-product'),
    path('delete-product/<int:product_id>/', DeleteProductView.as_view(), name='delete-product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('update-item/', update_item, name='update-item'),
]