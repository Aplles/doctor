from functools import lru_cache

from django import forms
from django.db.models import OuterRef, Subquery
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import ValidationError

from models_app.models import Product
from models_app.models import City
from models_app.models import ProductPrice


class ProductListService(ServiceWithResult):
    search = forms.CharField(required=False)
    categories_id = forms.CharField(required=False)
    localization = forms.CharField()

    custom_validations = ['check_categories_id', 'check_localization', 'check_approved_city']

    def process(self):
        self.run_custom_validations()
        self.result = self._products
        return self

    @property
    def _products(self):
        subquery = ProductPrice.objects.filter(
            product=OuterRef('pk'),
            city__localization=self.cleaned_data['localization']
        ).values('price', 'discount_price')

        products_from_city = self._city.products.annotate(
            price=Subquery(subquery.values('price')),
            discount_price=Subquery(subquery.values('discount_price')),
        ).all()

        products_from_country = self._city.country.products.annotate(
            price=Subquery(subquery.values('price')),
            discount_price=Subquery(subquery.values('discount_price'))
        ).all()

        return self._filter(
            products_from_city.union(products_from_country)
        ).order_by('-id')

    def _filter(self, queryset):
        if self.cleaned_data["search"]:
            queryset = queryset.filter(title__icontains=self.cleaned_data["search"])
        if self.cleaned_data["categories_id"]:
            queryset = queryset.filter(category__id__in=self.cleaned_data["categories_id"].split(','))
        return queryset

    @property
    @lru_cache
    def _city(self):
        try:
            return City.objects.select_related(
                'country'
            ).get(localization=self.cleaned_data['localization'])
        except City.DoesNotExist:
            return None

    def check_categories_id(self):
        categories_id = self.cleaned_data["categories_id"]
        if categories_id:
            try:
                list(map(int, categories_id.split(",")))
            except ValueError:
                raise ValidationError({
                    "detail": "The format of the submitted categories is not correct"
                })

    def check_localization(self):
        if not self._city:
            raise ValidationError({
                "detail": "No such localization exists"
            })

    def check_approved_city(self):
        if not self._city.is_approved:
            raise ValidationError({
                "detail": "This localization is not approved"
            })
