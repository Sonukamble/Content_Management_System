from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Content Model
class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='contents')
    author = models.ForeignKey(get_user_model(), related_name='contents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title