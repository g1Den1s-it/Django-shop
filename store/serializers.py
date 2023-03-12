from rest_framework import serializers

from .models import Subcategory, Category, Goods



class SubCategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'image_url', 'slug')

 
    def get_image_url(self, obj):
        req = self.context.get('request')
        image_url = obj.image.url
        return req.build_absolute_uri(image_url)


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta: 
        model = Category
        fields = ('id', 'name', 'image', 'slug', 'subcategory')


class GoodsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Goods
        fields = ('id', 'name', 'image_url', 
                  'price', 'description', 'subcategory')
        
    
    def get_image_url(self, obj):
        req = self.context.get('request')
        image_url = obj.image.url
        return req.build_absolute_uri(image_url)