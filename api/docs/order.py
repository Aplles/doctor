from drf_yasg import openapi
from rest_framework import status

from api.docs.error import VALIDATION_ERROR

ORDER_CREATE_VIEW = {
    "operation_id": "Создание заказа",
    "operation_description": """
    Создает новый заказ, как с услугами, так и без.
""",

    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "Success",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(),
            ),
        ),
        **VALIDATION_ERROR,
    },
}
