#create custom permision to aloud only admin to create, update and delete products
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff or user.is_superuser:
            return True