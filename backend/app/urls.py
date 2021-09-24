from rest_framework import routers
from .views import UserViewSet, OfferViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('offers', OfferViewSet)
router.register('categories', CategoryViewSet)
# router.register('user-offer', UserInfoViewSet)
