from drf_yasg import openapi
from rest_framework import status

from api.docs.error import VALIDATION_ERROR

PRODUCT_ITEM = {
    "items": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=dict(
            id=openapi.Schema(
                type=openapi.TYPE_INTEGER, example=1
            ),
            title=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            image=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            price=openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
            discount_price=openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
        ),
    ),
}

PRODUCT_LIST_VIEW = {
    "operation_id": "Список услуг",
    "operation_description": """
        Выводит список услуг на определённой странице
        Можно передать следующие аргументы:
        search - параметр поиска (ищет по полю title)
        page - номер страницы (по умолчанию 1)
        
        categories_id - id категорий, по которым нужно осуществить фильтрацию
        Пример передачи: /api/products/?categories_id=1,2,3
    """,
    'manual_parameters': [
        openapi.Parameter(
            'currency', openapi.IN_QUERY,
            description="Передайте валюту, чтобы получить необходимую цену",
            type=openapi.TYPE_STRING,
            required=True
        ),
        openapi.Parameter(
            'page', openapi.IN_QUERY,
            description="Вы можете указать номер страницы, с которой хотите получить данные",
            type=openapi.TYPE_NUMBER,
            required=False
        ),
        openapi.Parameter(
            'search', openapi.IN_QUERY,
            description="Вы можете передать строчку для поиска",
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'categories_id', openapi.IN_QUERY,
            description="Вы можете передать id категорий, по которым необходимо отфильтровать через запятую",
            type=openapi.TYPE_STRING,
            required=False
        ),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    count=openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    next=openapi.Schema(type=openapi.TYPE_STRING, example='null'),
                    previous=openapi.Schema(type=openapi.TYPE_STRING, example='null'),
                    results=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        **PRODUCT_ITEM,
                    ),
                ),
            ),
        ),
        **VALIDATION_ERROR,
    },
}
