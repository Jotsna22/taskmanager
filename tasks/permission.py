from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for all, but restrict list access to admins
        if request.method == "GET":
            return (
                request.user and request.user.is_staff
            )  # Only admins can list all tasks
        return True  # Allow other requests
