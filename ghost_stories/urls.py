from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls'), name='homepage-urls'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('stories/', include('stories.urls'), name='stories-urls'),
    path('users/', include('profiles.urls'), name='user-urls'),
]

handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
