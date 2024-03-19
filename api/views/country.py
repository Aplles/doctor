from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView

from api.docs.country import COUNTRY_LIST_VIEW
from api.serializers.country.list import CountryListSerializer
from models_app.models import Country


class CountryListView(ListAPIView):
    serializer_class = CountryListSerializer
    pagination_class = None

    def get_queryset(self):
        return Country.objects.all()

    @swagger_auto_schema(**COUNTRY_LIST_VIEW)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
