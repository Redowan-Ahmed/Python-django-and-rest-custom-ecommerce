from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/',include('playground.urls')),
    path('store/',include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)