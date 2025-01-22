from rest_framework import serializers
from .models import Content, Category
from django.contrib.auth import get_user_model

class ContentSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'summary', 'categories', 'author']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
