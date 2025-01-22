from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Content, Category
from .serializers import ContentSerializer
from django.contrib.auth import get_user_model

# Permissions for Authors and Admins
class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'DELETE', 'PUT']:
            if request.user.is_staff:  # Admin can access all
                return True
            return obj.author == request.user  # Author can only access their content
        return False

# Create Content
@api_view(['POST'])
@permission_classes([IsAuthorOrAdmin])
def create_content(request):
    if request.user.is_authenticated and request.user.role == 'author':
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Save with logged-in user as author
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get All Content (Admin sees all, Author sees their own)
@api_view(['GET'])
@permission_classes([IsAuthorOrAdmin])
def get_content(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            contents = Content.objects.all()
        else:
            contents = Content.objects.filter(author=request.user)
        
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

# Search Content by Title, Body, Summary, and Categories
@api_view(['GET'])
def search_content(request):
    query = request.GET.get('query', '')
    if query:
        results = Content.objects.filter(
            title__icontains=query
        ) | Content.objects.filter(
            body__icontains=query
        ) | Content.objects.filter(
            summary__icontains=query
        ) | Content.objects.filter(
            categories__name__icontains=query
        )
        serializer = ContentSerializer(results, many=True)
        return Response(serializer.data)
    return Response({'detail': 'Query parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

# Edit Content (Only the author or admin can edit)
@api_view(['PUT'])
@permission_classes([IsAuthorOrAdmin])
def edit_content(request, pk):
    try:
        content = Content.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user == content.author or request.user.is_staff:
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

# Delete Content (Only the author or admin can delete)
@api_view(['DELETE'])
@permission_classes([IsAuthorOrAdmin])
def delete_content(request, pk):
    try:
        content = Content.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.user == content.author or request.user.is_staff:
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
