from rest_framework import serializers
from .models import User, Offer, Category, UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # category_id = serializers.ChoiceField(choices=list(Category.objects.all().values_list('name', flat=True)))

    class Meta:
        model = Offer
        fields = '__all__'
        # exclude = ['category']

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        category = Category.objects.get_or_create(**category_data)[0]
        validated_data['category'] = category
        return Offer.objects.create(**validated_data)


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
