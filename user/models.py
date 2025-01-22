from django.db import models

# Create your models here.
# cms/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from .manager import CustomUserManager

class User(AbstractUser):
    # Adding unique email for login
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    # Additional fields as per requirements
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits")],
        blank=True,
        null=True
    )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator(regex=r'^\d{6}$', message="Pincode must be 6 digits")],
        blank=True,
        null=True
    )
    # Role choices
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('author', 'Author'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='author')

    objects = CustomUserManager()

    # Use email for login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone', 'pincode']

    def __str__(self):
        return self.email
