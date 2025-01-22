# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.view_all_users, name='view_all_users'),  # Admin can view all users
    path('api/users/<int:id>/', views.edit_user, name='edit_user'),  # Admin can edit user
    path('api/users/<int:id>/', views.delete_user, name='delete_user'),  # Admin can delete user
]
