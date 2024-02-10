from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.docs.nurse import NURSE_PROMO_CODE_PRESENCE_VIEW, NURSE_CREATE_VIEW
from api.serializers.nurse.create import NurseCreateSerializer
from api.serializers.nurse.promo_code import NursePromoCodeSerializer
from models_app.models import Nurse


class NurseCreateView(CreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseCreateSerializer

    @swagger_auto_schema(**NURSE_CREATE_VIEW)
    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)


class NursePromoCodePresenceView(RetrieveAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NursePromoCodeSerializer
    lookup_field = 'promo_code'

    @swagger_auto_schema(**NURSE_PROMO_CODE_PRESENCE_VIEW)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
