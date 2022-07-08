from django.contrib import admin
from .models import Album, Favorite, User


admin.site.register(Album)
admin.site.register(Favorite)
admin.site.register(User)
#admin.site.register(Artist)
