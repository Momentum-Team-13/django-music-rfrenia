"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from RyansMusic import views as RyansMusic_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RyansMusic_views.list_albums, name='list_albums'),
    path('RyansMusic/new/', RyansMusic_views.add_album, name='add_album'),
    path('RyansMusic/<int:pk>', RyansMusic_views.album_detail, name='album_detail'),
    path('RyansMusic/<int:pk>/edit', RyansMusic_views.edit_album, name='edit_album'),
    path('RyansMusic/<int:pk>/delete', RyansMusic_views.delete_album, name='delete_album'),
    path('RyansMusic/<int:pk>/add_fav', RyansMusic_views.add_favorite, name='add_favorite'),
    path('RyansMusic/<int:pk>/delete_fav', RyansMusic_views.delete_favorite, name='delete_favorite'),
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)