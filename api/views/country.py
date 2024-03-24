from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.country import COUNTRY_LIST_VIEW
from api.serializers.country.list import CountrySerializer
from api.services.country.show import CountryShowService
from models_app.models import Country


class CountryListView(ListAPIView):
    serializer_class = CountrySerializer
    pagination_class = None

    def get_queryset(self):
        return Country.objects.all()

    @swagger_auto_schema(**COUNTRY_LIST_VIEW)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CountryShowView(RetrieveAPIView):
    serializer_class = CountrySerializer

    def get_object(self):
        return ServiceOutcome(CountryShowService, self.kwargs).result
