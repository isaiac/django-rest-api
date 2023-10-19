from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import User
from ..permissions import UserPermission
from ..serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, UserPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['username', 'email']
    ordering = ['-date_joined']
