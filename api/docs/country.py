from drf_yasg import openapi
from rest_framework import status

from api.docs.city import CITY_ITEM, CITY_ITEM_PROPERTIES

COUNTRY_LIST_VIEW = {
    "operation_id": "Список стран и городов",
    "operation_description": """
    Выводит список стран и их городов
""",
    'manual_parameters': [
        openapi.Parameter(
            'search', openapi.IN_QUERY,
            description="Вы можете передать строчку для поиска",
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
                    id=openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                    name=openapi.Schema(type=openapi.TYPE_STRING, example='string'),
                    localization=openapi.Schema(type=openapi.TYPE_STRING, example='string'),
                    cities=openapi.Schema(type=openapi.TYPE_ARRAY, **CITY_ITEM),
                    default_city=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        **CITY_ITEM_PROPERTIES
                    ),
                ),
            ),
        ),
    },
}
