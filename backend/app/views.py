from django_filters import rest_framework
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Offer, Category, UserInfo
from .utils.auth import NormalAuthentication, JWTAuthentication
from .serializer import UserSerializer, OfferSerializer, CategorySerializer


class Login(APIView):
    authentication_classes = [NormalAuthentication]

    def post(self, request, *args, **kwargs):
        return Response({'token': request.user})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    # filter_fields = ('item_name', 'item_date')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class UserInfoViewSet(viewsets.ModelViewSet):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
