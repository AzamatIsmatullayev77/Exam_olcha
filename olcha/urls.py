from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from olcha.views import (
    Category1ViewSet, CategoryViewSet, ProductViewSet,
    ImageViewSet, CommentViewSet
)

router = DefaultRouter()
router.register(r'categories1', Category1ViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ImageViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
