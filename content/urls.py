from django.urls import path
from . import views

urlpatterns = [
    path('api/content/', views.create_content, name='create_content'),
    path('api/getcontent/', views.get_content, name='get_content'),
    path('api/content/search/', views.search_content, name='search_content'),
    path('api/content/<int:pk>/', views.edit_content, name='edit_content'),
    path('api/content/<int:pk>/', views.delete_content, name='delete_content'),
]
