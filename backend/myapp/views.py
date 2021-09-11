from django_filters import rest_framework
from rest_framework import viewsets, filters
from .models import User, Offer
from .serializer import UserSerializer, OfferSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_fields = ('item_name', 'item_date')
