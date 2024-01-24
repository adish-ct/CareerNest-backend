from rest_framework import permissions


class IsRecruiterPermission(permissions.BasePermission):
    """
        allows only recruiter to be granted
    """

    def has_permission(self, request, view):
        # check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # check if the user is a recruiter
        if request.user.role.role == "Employer":
            return True
        
        return False
        
