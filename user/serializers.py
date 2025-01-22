from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Custom User Serializer (for registration)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'full_name', 'phone', 'address', 'city', 'state', 'country', 'pincode']

    def validate_password(self, value):
        if not any(char.islower() for char in value):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in value):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least one digit.")
        return value
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.username = user.email
        if not user.username:
            user.username = user.email
        user.set_password(password)
        user.save()
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = None
        try:
            user = get_user_model().objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError('Invalid credentials.')
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Invalid credentials.')

        return {'user': user}
