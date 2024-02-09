from drf_yasg import openapi

CATEGORY_ITEM = {
    "items": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=dict(
            id=openapi.Schema(
                type=openapi.TYPE_INTEGER, example=1
            ),
            title=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        ),
    ),
}