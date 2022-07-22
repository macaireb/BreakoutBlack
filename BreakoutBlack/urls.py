from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("store.urls", namespace="store")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
