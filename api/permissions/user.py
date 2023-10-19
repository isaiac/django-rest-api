from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        auth_user = request.user

        if view.action == 'list':
            return auth_user.has_perm('auth.view_user')

        if view.action == 'create':
            return auth_user.has_perm('auth.add_user')

        return view.action in ['retrieve', 'update', 'partial_update', 'destroy']

    def has_object_permission(self, request, view, obj):
        auth_user = request.user

        if view.action == 'retrieve':
            return auth_user.has_perm('auth.view_user')

        if view.action in ['update', 'partial_update']:
            return auth_user.has_perm('auth.change_user')

        if view.action == 'destroy':
            return auth_user.has_perm('auth.delete_user')

        return False
