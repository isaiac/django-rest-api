from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_active'] = user.is_active

        return token
