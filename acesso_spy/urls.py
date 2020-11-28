from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from acessos import urls as acessos_urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(acessos_urls)),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('admin_spy/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
