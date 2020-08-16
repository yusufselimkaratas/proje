from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class OwnerPermission(BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj.user == request.user