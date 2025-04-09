from rest_framework import serializers
from olcha.models import Product,Images,Category,Category1
from olcha.views import Comment


class Category1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        exclude = ()


class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    likes = serializers.SerializerMethodField()
    def get_likes(self, instance):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        if user not in instance.likes.all():
            return False
        return True
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField()

    def get_product_title(self, obj):
        return obj.product_title
    class Meta:
        model = Comment
        fields = '__all__'