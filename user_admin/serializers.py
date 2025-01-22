
# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'full_name', 'role', 'phone', 'pincode', 'is_staff', 'is_superuser']
