from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.city.show import CityShowSerializer
from api.services.city.show import CityShowService


class CityShowView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CityShowService, kwargs)
        return Response(CityShowSerializer(outcome.result).data)
