from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import *

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
