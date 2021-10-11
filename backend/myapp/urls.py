
from django.urls import path, include
from myapp import views
from rest_framework.routers import DefaultRouter
from .views import SignupViewSet, OfferViewSet, CategoryViewSet, ProfileViewSet, ClientShopViewSet, AssesmentPriceViewSet


app_name='user'

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('signup', SignupViewSet)
router.register('offers', OfferViewSet)
router.register('categories', CategoryViewSet)
router.register('client', ClientShopViewSet)
router.register('assesment_price', AssesmentPriceViewSet)
# router.register('user-offer', UserInfoViewSet)


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('myself/', views.ManageUserView.as_view(), name='myself'),
    path('', include(router.urls))
]