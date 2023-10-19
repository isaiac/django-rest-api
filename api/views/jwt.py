from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..serializers.jwt import JWTObtainPairSerializer


class JWTObtainPairView(TokenObtainPairView):
    throttle_scope = 'login'
    serializer_class = JWTObtainPairSerializer


class JWTRefreshView(TokenRefreshView):
    throttle_scope = 'token-refresh'
