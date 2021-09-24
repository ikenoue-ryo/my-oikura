from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from app.views import Login

from app.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen/', views.obtain_auth_token),
    path('api/v1/api/', include(router.urls)),
    path('api/v1/login/', Login.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]


# 開発環境でのメディアファイルの配信設定
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
