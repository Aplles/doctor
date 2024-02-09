from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from service_objects.services import ServiceOutcome

from api.docs.product import PRODUCT_LIST_VIEW
from api.serializers.product.list import ProductListSerializer
from api.services.product.list import ProductListService


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return ServiceOutcome(ProductListService, self.request.query_params).result

    @swagger_auto_schema(**PRODUCT_LIST_VIEW)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
