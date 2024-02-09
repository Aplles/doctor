from drf_yasg import openapi
from rest_framework import status

NOT_FOUND_ERROR = {
    404: openapi.Response(
        'NotFound',
        openapi.Schema(
            title="Error Not Found",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                type=openapi.Schema(type=openapi.TYPE_STRING, example="NotFound"),
                message=openapi.Schema(type=openapi.TYPE_STRING, example="Resource not found"),
                translation_key=openapi.Schema(type=openapi.TYPE_STRING, example="not_found"),
            ),
        ),
    )
}

VALIDATION_ERROR = {
    400: openapi.Response(
        'Bad request',
        openapi.Schema(
            title="ValidationError",
            type=openapi.TYPE_OBJECT,
            properties=dict(
                type=openapi.Schema(type=openapi.TYPE_STRING, example="ValidationError"),
                message=openapi.Schema(type=openapi.TYPE_STRING, example="Validation error on data"),
                translation_key=openapi.Schema(type=openapi.TYPE_STRING, example="validation_error"),
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
                type=openapi.Schema(type=openapi.TYPE_STRING, example="AccessDenied"),
                message=openapi.Schema(type=openapi.TYPE_STRING, example="Access denied"),
                translation_key=openapi.Schema(type=openapi.TYPE_STRING, example="access_denied"),
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
                type=openapi.Schema(type=openapi.TYPE_STRING, example="ForbiddenError"),
                message=openapi.Schema(type=openapi.TYPE_STRING, example="Not enough rights"),
                translation_key=openapi.Schema(type=openapi.TYPE_STRING, example="forbidden"),
            ),
        ),
    )
}
