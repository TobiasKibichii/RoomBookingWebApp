from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        # Allow read-only access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Admins can do anything
        if request.user.is_staff or request.user.is_superuser:
            return True
        
        return obj.user == request.user
    

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_superuser
    
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_superuser