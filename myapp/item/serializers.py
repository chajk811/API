from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    imgUrl = serializers.CharField(source='imageId')

    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales',)


class RecommendSerializer(serializers.ModelSerializer):
    imgUrl = serializers.CharField(source='imageId')

    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price',)