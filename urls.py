from django.conf import settings
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
