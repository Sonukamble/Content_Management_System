from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer


class RegisterAuthor(APIView):
    """
    Register an author user.
    """
    permission_classes = [permissions.AllowAny]  # No authentication required to register

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(role='author')
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    User login and token generation.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)
            return Response({
                'token': str(token.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
