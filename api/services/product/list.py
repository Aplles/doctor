from django import forms
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import ValidationError

from models_app.models import Product


class ProductListService(ServiceWithResult):
    search = forms.CharField(required=False)
    categories_id = forms.CharField(required=False)

    custom_validations = ['check_categories_id']

    def process(self):
        self.run_custom_validations()
        self.result = self._products
        return self

    @property
    def _products(self):
        products = self._filter(Product.objects.all())
        return products.order_by('-id')

    def _filter(self, queryset):
        if self.cleaned_data["search"]:
            queryset = queryset.filter(title__icontains=self.cleaned_data["search"])
        if self.cleaned_data["categories_id"]:
            queryset = queryset.filter(category_id__in=self.cleaned_data["categories_id"].split(','))
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
