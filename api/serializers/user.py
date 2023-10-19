from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from ..models import Group, Permission, User


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = {**super().to_representation(instance)}

        return {
            'id': data['id'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'username': data['username'],
            'is_staff': data['is_staff'],
            'is_superuser': data['is_superuser'],
            'is_active': data['is_active'],
            'last_login': data['last_login'],
            'date_joined': data['date_joined'],
            'groups': GroupSerializer(instance=instance.groups, many=True).data,
            'permissions': PermissionSerializer(
                instance=instance.user_permissions, many=True
            ).data,
        }

    class Meta:
        model = User
        fields = '__all__'
