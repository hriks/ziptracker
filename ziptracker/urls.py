from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from settings import MEDIA_URL, MEDIA_ROOT
from pincode import apis

urlpatterns = [
    url(r'^pincode/(?P<pk>[A-Za-z_0-9\-]+)$', apis.GetPincode.as_view()),
    url(r'^admin/', admin.site.urls),
] + static(
    MEDIA_URL, document_root=MEDIA_ROOT)
