from django.contrib.auth.models import Group as AuthGroup


class Group(AuthGroup):
    class Meta:
        proxy = True
