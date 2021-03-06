from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

from users.permissions import UserPermission
from users.seriealizers import UserSerializer, UserListSerializer

from django.shortcuts import get_object_or_404


class UserListAPI(APIView):

    permission_classes = (UserPermission,)
    def get(self, request):
        users = User.objects.all()
        serialzar = UserListSerializer(users, many=True)
        return Response(serialzar.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    """
    Endpoint del detalle de un usuario.
    """
    permission_classes = (UserPermission,)
    def get(self, request , pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

