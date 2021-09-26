from django_filters import rest_framework
from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from myapp import serializers
from .models import User, Offer, Category, Profile

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from myapp import ownpermissions
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils.auth import NormalAuthentication, JWTAuthentication
from .serializers import UserSerializer, OfferSerializer, CategorySerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    authentication_class = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, ownpermissions.ProfilePermission)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError("User can have only one own profile")


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
