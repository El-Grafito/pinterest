from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_staff

class CustomUserDetailsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff

class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_staff

class CategoryDetailsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_authenticated

class PostDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated