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
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    summary = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title