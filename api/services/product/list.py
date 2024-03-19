from django import forms
from django.db.models import OuterRef, Subquery
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import ValidationError

from models_app.models import Product
from models_app.models import Currency
from models_app.models import ProductPrice


class ProductListService(ServiceWithResult):
    search = forms.CharField(required=False)
    categories_id = forms.CharField(required=False)
    currency = forms.CharField()

    custom_validations = ['check_categories_id', 'check_currency']

    def process(self):
        self.run_custom_validations()
        self.result = self._products
        return self

    @property
    def _products(self):
        subquery = ProductPrice.objects.filter(
            product=OuterRef('pk'),
            currency__value=self.cleaned_data['currency']
        ).values('price', 'discount_price')
        products = self._filter(Product.objects.annotate(
            price=Subquery(subquery.values('price')),
            discount_price=Subquery(subquery.values('discount_price')),
        ).all())
        return products.order_by('-id')

    def _filter(self, queryset):
        if self.cleaned_data["search"]:
            queryset = queryset.filter(title__icontains=self.cleaned_data["search"])
        if self.cleaned_data["categories_id"]:
            queryset = queryset.filter(category__id__in=self.cleaned_data["categories_id"].split(','))
        return queryset

    def check_categories_id(self):
        categories_id = self.cleaned_data["categories_id"]
        if categories_id:
            try:
                list(map(int, categories_id.split(",")))
            except ValueError:
                raise ValidationError({
                    "detail": "The format of the submitted categories is not correct"
                })

    def check_currency(self):
        if self.cleaned_data['currency'] not in list(
                map(
                    lambda x: x[0],
                    list(
                        Currency.objects.all().values_list('value')
                    )
                )
        ):
            raise ValidationError({
                "detail": "No such currency exists"
            })
