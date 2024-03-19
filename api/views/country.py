from rest_framework.generics import ListAPIView

from api.serializers.country.list import CountryListSerializer
from models_app.models import Country


class CountryListView(ListAPIView):
    serializer_class = CountryListSerializer

    def get_queryset(self):
        return Country.objects.filter()

    # @swagger_auto_schema(**PRODUCT_LIST_VIEW)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
