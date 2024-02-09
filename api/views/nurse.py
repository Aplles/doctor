from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.serializers.nurse.create import NurseCreateSerializer
from models_app.models import Nurse


class NurseCreateView(CreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseCreateSerializer

    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)


class PromoCodePresenceView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        pass
