from rest_framework import serializers
from .models import User, Offer, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Offer
        fields = '__all__'
