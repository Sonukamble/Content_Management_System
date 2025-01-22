from django.contrib.auth.models import BaseUserManager


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, full_name, phone, pincode, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, phone=phone, pincode=pincode, **extra_fields)
        if not user.username:
            user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name, phone, pincode, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, full_name, phone, pincode=pincode, **extra_fields)