from django import forms
from .models import Product, ShippingAddress


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nazwa',
                                           }),
            'producer': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Producent',
                                               }),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Opis',
                                                 }),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                              'placeholder': 'Cena',
                                              }),
            'discount_price': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Promocyjna cena',
                                              }),
            'image': forms.FileInput(attrs={'class': 'form-control',
                                            }),
        }
        labels = {
            'name': '',
            'producer': '',
            'description': '',
            'price': '',
            'discount_price': '',
            'image': '',
        }

