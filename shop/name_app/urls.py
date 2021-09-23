from django.urls import path
from .views import IndexView, ProductsView

app_name = 'name_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),


]

