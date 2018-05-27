from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from settings import MEDIA_URL, MEDIA_ROOT
from pincode import views

urlpatterns = [
    url(r'^ziptracker', views.ziptracker, name='ziptracker'),
    url(r'^admin/', admin.site.urls),
] + static(
    MEDIA_URL, document_root=MEDIA_ROOT)
