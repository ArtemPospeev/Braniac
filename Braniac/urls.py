from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include('django.conf.urls.i18n')),
    path("", include("mainapp.urls", namespace='mainapp')),
    path("authapp/", include("authapp.urls", namespace='authapp')),
    path('social_auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))  # Подключение debug toolbar'a
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Добавления MEDIA_URL'a
