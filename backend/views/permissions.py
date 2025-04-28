
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to only allow admins to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is an admin
        return bool(request.user and request.user.role == 'admin')

class IsDirector(BasePermission):
    """
    Custom permission to only allow directors to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a director
        return bool(request.user and request.user.role == 'director')
    
class IsAgency(BasePermission):
    """
    Custom permission to only allow agency users to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is an agency user
        return bool(request.user and request.user.role == 'agency')    