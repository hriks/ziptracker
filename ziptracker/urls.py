from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    url(r'^hriks/handle/', admin.site.urls),
] + static(
    MEDIA_URL, document_root=MEDIA_ROOT)
