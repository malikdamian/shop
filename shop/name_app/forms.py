from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, ButtonHolder, Submit
from django import forms
from .models import Product, ShippingAddress


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'producer': 'Producent',
            'description': 'Opis',
            'price': 'Cena',
            'discount_price': 'Cena promocyjna',
            'image': 'Zdjęcie',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj produkt',
            ),
            Row(
                Column('name'),
                Column('producer'),
            ),
            Row(
                Column('price'),
                Column('discount_price'),
                Column('image'),
            ),
            'description',
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-success'),

            ),

        )
