from rest_framework import permissions


class IsVendedor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo_usuario == 'VENDEDOR'
    

class IsCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo_usuario == 'CLIENTE'
