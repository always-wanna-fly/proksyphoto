from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^', include('gallery.urls')),
    url(r'^', include('about_me.urls')),
    url(r'^', include('my_contact.urls')),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
