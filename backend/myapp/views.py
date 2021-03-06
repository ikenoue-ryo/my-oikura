from django_filters import rest_framework
from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from myapp import serializers
from .models import User, Offer, Category, Profile, ClientShop, AssesmentPrice, ClientMessage, Car, ShopReview, VisitReservation, ClientPr, Like, Brand

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
from .serializers import UserSerializer, OfferSerializer, CategorySerializer, AssesmentPriceSerializer, ClientMessageSerializer, ShopReviewSerializer, VisitReservationSerializer, ClientPrSerializer, LikeSerializer, BrandSerializer


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
    # authentication_class = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, ownpermissions.ProfilePermission)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError("User can have only one own profile")


# class Login(APIView):
#     authentication_classes = [NormalAuthentication]

#     def post(self, request, *args, **kwargs):
#         return Response({'token': request.user})


class SignupViewSet(viewsets.ModelViewSet):
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

class ClientShopViewSet(viewsets.ModelViewSet):
    queryset = ClientShop.objects.all()
    serializer_class = serializers.ClientShopSerializer
    # authentication_class = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, ownpermissions.ClientShopPermission)


class AssesmentPriceViewSet(viewsets.ModelViewSet):
    queryset = AssesmentPrice.objects.all()
    serializer_class = serializers.AssesmentPriceSerializer


class ClientMessageViewSet(viewsets.ModelViewSet):
    queryset = ClientMessage.objects.all()
    serializer_class = serializers.ClientMessageSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(sender=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(sender=self.request.user)


class InboxListView(generics.ListAPIView):

    queryset = ClientMessage.objects.all()
    serializer_class = serializers.ClientMessageSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(receiver=self.request.user)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class ShopReviewViewSet(viewsets.ModelViewSet):
    queryset = ShopReview.objects.all()
    serializer_class = serializers.ShopReviewSerializer


class VisitReservationViewSet(viewsets.ModelViewSet):
    queryset = VisitReservation.objects.all()
    serializer_class = serializers.VisitReservationSerializer


class ClientPrViewSet(viewsets.ModelViewSet):
    queryset = ClientPr.objects.all()
    serializer_class = serializers.ClientPrSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
