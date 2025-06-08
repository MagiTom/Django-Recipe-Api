from django.urls import path
from .views import CustomLoginView, RegisterView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="custom_login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('user/', UserView.as_view(), name='user-view'),

]


