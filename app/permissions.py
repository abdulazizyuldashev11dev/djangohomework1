from rest_framework.permissions import BasePermission

class StaffPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True
        return False

class AdminPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3:
            return True
        print(request.user.roles)
        return False
class OwnerPermissionClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
        return False