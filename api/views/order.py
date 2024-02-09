from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.docs.order import ORDER_CREATE_VIEW
from api.serializers.order.create import OrderCreateSerializer
from models_app.models import Order


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    @swagger_auto_schema(**ORDER_CREATE_VIEW)
    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
