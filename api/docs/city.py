from drf_yasg import openapi

CITY_ITEM_PROPERTIES = {
    "properties": dict(
        id=openapi.Schema(
            type=openapi.TYPE_INTEGER, example=1
        ),
        name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        localization=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
    ),
}

CITY_ITEM = {
    "items": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        **CITY_ITEM_PROPERTIES
    ),
}
