from django.contrib import admin
from django.urls import path, include
import Dev_app.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dev_app.views.home, name="index"),
    path('login/', Dev_app.views.login, name="login"),
    path('register/', Dev_app.views.Register.as_view(), name="register"),
    path('logout/', Dev_app.views.logout, name="logout"),
    path('image/', Dev_app.views.post_text, name="image"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
