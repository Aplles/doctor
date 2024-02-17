from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.category.show import CategorySerializer
from models_app.models import Category


class CategoryListView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(CategorySerializer(
            Category.objects.filter(products__isnull=False).distinct(),
            many=True
        ).data)
