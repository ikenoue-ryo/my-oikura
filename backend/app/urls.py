from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OfferViewSet, CategoryViewSet, ProfileViewSet


app_name='user'

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('users', UserViewSet)
router.register('offers', OfferViewSet)
router.register('categories', CategoryViewSet)
# router.register('user-offer', UserInfoViewSet)


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('myself/', views.ManageUserView.as_view(), name='myself'),
    path('', include(router.urls))
]