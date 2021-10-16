from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User, Offer, Category, Profile, ClientShop, AssesmentPrice, ClientMessage, Car


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    profile = ProfileSerializer()
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


# 循環参照回避
class ClientShopsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientShop
        fields = '__all__'


class AssesmentPriceSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()
    client_shop = ClientShopsSerializer()
    
    class Meta:
        model = AssesmentPrice
        fields = '__all__'


class ClientShopSerializer(serializers.ModelSerializer):
    client = ClientShop()
    assesment_price = AssesmentPriceSerializer()

    class Meta:
        model = ClientShop
        fields = '__all__'


class ClientMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = ClientMessage
        fields = '__all__'
        read_only_fields = ('id', 'sender')


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
