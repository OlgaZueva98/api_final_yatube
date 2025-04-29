from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверяет, что пользователь не может изменять и удалять чужие данные."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
