from drf_yasg import openapi
from rest_framework import status

NOT_FOUND_ERROR = {
    404: openapi.Response(
        'Not Found',
        openapi.Schema(
            title="Error Not Found",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                detail=openapi.Schema(type=openapi.TYPE_STRING, example="NotFound")
            ),
        ),
    )
}

VALIDATION_ERROR = {
    400: openapi.Response(
        'Validation Error',
        openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                detail=openapi.Schema(type=openapi.TYPE_STRING, example="ValidationError")
            ),
        ),
    )
}

ACCESS_DENIED = {
    status.HTTP_409_CONFLICT: openapi.Response(
        'Locked',
        openapi.Schema(
            title="AccessDenied",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                detail=openapi.Schema(type=openapi.TYPE_STRING, example="AccessDenied")
            ),
        ),
    )
}

FORBIDDEN_ERROR = {
    status.HTTP_403_FORBIDDEN: openapi.Response(
        'Forbidden',
        openapi.Schema(
            title="ForbiddenError",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                detail=openapi.Schema(type=openapi.TYPE_STRING, example="ForbiddenError")
            ),
        ),
    )
}
