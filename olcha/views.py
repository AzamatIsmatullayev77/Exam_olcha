from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from olcha.models import Product, Images, Comment, Category1, Category
from olcha.serializers import (
    ProductModelSerializer, ImageSerializer, CommentSerializer,
    CategorySerializer, Category1Serializer
)

class Category1ViewSet(viewsets.ModelViewSet):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



from rest_framework.decorators import action
from rest_framework.response import Response

class CommentByProductViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def list_by_product(self, request, pk=None):
        comments = Comment.objects.filter(product_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
