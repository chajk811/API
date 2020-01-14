from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    imageUrl = serializers.CharField(source='imageId')

    class Meta:
        model = Item
        fields = ('id', 'imageUrl', 'name', 'price', 'ingredients', 'monthlySales',)


class RecommendSerializer(serializers.ModelSerializer):
    imageUrl = serializers.CharField(source='imageId')

    class Meta:
        model = Item
        fields = ('id', 'imageUrl', 'name', 'price',)