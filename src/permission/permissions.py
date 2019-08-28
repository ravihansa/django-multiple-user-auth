from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    """
    Allows access only to "is_customer" users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_customer and request.user.is_active


class IsMerchant(BasePermission):
    """
    Allows access only to "is_merchant" users.
    """
    message = 'Only merchants have permission to perform this action.'

    def has_permission(self, request, view):
        return request.user and request.user.is_merchant and request.user.is_active
