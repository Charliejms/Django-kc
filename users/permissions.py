from rest_framework.permissions import BasePermission




class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un ususrio puede ejecutar el metodo o acceder a la vista/controlador que quiere acceder
        :param request:
        :param view:
        :return:
        """
        from users.api import UserDetailAPI
        if request.method == "POST":
            return True
        if request.user.is_superuser:
            return True
        if isinstance(view, UserDetailAPI):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usurio puede realizar la opicion que quiere con el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user ==obj