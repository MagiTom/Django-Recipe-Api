from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet, CategoryViewSet, test_view

router = DefaultRouter()
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("users.urls")),  
    path("api/test/", test_view),  
]
