from rest_framework import serializers
from .models import User, Offer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class OfferSerializer(serializers.ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Offer
        fields = '__all__'
