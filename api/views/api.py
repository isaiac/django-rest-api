from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ping(_):
    return Response(
        {
            'status_code': 200,
            'message': f'Welcome to {settings.APP_NAME}!',
            'data': None,
        }
    )
