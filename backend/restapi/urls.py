from django.contrib import admin
from django.urls import path, include

from myapp.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
