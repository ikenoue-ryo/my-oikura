from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapp.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# 開発環境でのメディアファイルの配信設定
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
