from service_objects.services import ServiceWithResult
from service_objects.fields import DictField

from models_app.models import Order, ProductAmount


class OrderCreateService(ServiceWithResult):
    validated_data = DictField()

    def process(self):
        products = self._products
        self.result = self._order
        self._create_products(self.result, products)
        return self

    @property
    def _order(self):
        return Order.objects.create(**self.cleaned_data["validated_data"])

    @property
    def _products(self):
        if self.cleaned_data["validated_data"].get("products"):
            return self.cleaned_data["validated_data"].pop("products")

    @staticmethod
    def _create_products(order, products):
        if products:
            ProductAmount.objects.bulk_create(
                [
                    ProductAmount(
                        amount=int(product['amount']),
                        order=order,
                        product=product['id'],
                    )
                    for product in products
                ]
            )
