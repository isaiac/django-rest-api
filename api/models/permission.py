from django.contrib.auth.models import Permission as AuthPermission


class Permission(AuthPermission):
    class Meta:
        proxy = True
