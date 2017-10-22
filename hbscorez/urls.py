from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from associations import views as assoc
from base.views import notice, home, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^impressum', notice, name='notice'),
    url(r'^kontakt$', contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^verbaende/$', assoc.associations, name='assocs'),
    url(r'^(?P<assoc_abbr>[a-z]+)/', include('associations.urls', namespace='assoc')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
