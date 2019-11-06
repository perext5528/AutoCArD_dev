from django.contrib import admin
from django.urls import path, include
import Dev_app.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dev_app.views.home, name="home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
