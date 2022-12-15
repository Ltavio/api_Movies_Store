from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Users


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsAuthenticateOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Users) -> bool:
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated:
            return obj == request.user

        return False
