# django_app/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('generate-random-user/', UserViewSet.as_view({'post': 'create_random_user'}), name='generate_random_user'),
] + router.urls
