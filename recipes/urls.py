from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, CategoryViewSet
from .views import test_view

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
    path('test/', test_view)
]
