from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Check the user has a permission to update his own profile"""

    def has_object_permission(self, request , view, obj):
        """check permission"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id

class PostOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.userprofile.id==request.user.id
