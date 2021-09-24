from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class ProductsView(View):

    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            products = Product.objects.filter(Q(name__icontains=search) |
                                              Q(producer__icontains=search))
        else:
            products = Product.objects.all()
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'products.html', {'page_obj': page_obj,
                                                 'search': search})


class ProductView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        products = Product.objects.filter(producer__icontains=product.producer)
        return render(request, 'product.html', {'product': product,
                                                'products': products})

