from drf_yasg import openapi
from rest_framework import status

from api.docs.error import NOT_FOUND_ERROR

NURSE_PROMO_CODE_PRESENCE_VIEW = {
    "operation_id": "Проверка промокода",
    "operation_description": """
    Проверяет наличие промокода в базе данных
""",

    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    id=openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                    first_name=openapi.Schema(type=openapi.TYPE_STRING, example='string'),
                    promo_code=openapi.Schema(type=openapi.TYPE_STRING, example='string'),
                ),
            ),
        ),
        **NOT_FOUND_ERROR,
    },
}

NURSE_CREATE_VIEW = {
    "operation_id": "Регистрация медсестры",
    "operation_description": """
    Регистрирует новую медсестру
""",

    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "Success",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(),
            ),
        ),
        **NOT_FOUND_ERROR,
    },
}
