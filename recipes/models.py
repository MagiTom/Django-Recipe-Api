from django.db import models
from recipe_app.storage_backends import SupabaseMediaStorage
from users.models import CustomUser

class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="categories/",
        storage=SupabaseMediaStorage(),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=200)
    url = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        upload_to="recipes/",
        storage=SupabaseMediaStorage(),
        null=True,
        blank=True
    )
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title