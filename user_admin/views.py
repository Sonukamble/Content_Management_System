from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Admin Permission to View All Users
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

# View All Users (Admin only)
@api_view(['GET'])
@permission_classes([IsAdmin])
def view_all_users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# views.py
@api_view(['PUT'])
@permission_classes([IsAdmin])
def edit_user(request, id):
    try:
        user = get_user_model().objects.get(id=id)
    except get_user_model().DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
@api_view(['DELETE'])
@permission_classes([IsAdmin])
def delete_user(request, id):
    try:
        user = get_user_model().objects.get(id=id)
    except get_user_model().DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
