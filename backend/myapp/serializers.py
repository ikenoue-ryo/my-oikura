from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User, Offer, Category, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'user', 'created_on', 'img')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # profile_user = ProfileSerializer()
    # profile_id = serializers.ChoiceField(choices=list(Profile.objects.all().values_list('nickname', flat=True)))
    
    class Meta:
        model = Offer
        fields = '__all__'
        # exclude = ['profile']

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        category = Category.objects.get_or_create(**category_data)[0]
        validated_data['category'] = category

        # user_data = validated_data.pop('user', None)
        # user = User.objects.get_or_create(**user_data)[0]
        # validated_data['user'] = user
        return Offer.objects.create(**validated_data)

