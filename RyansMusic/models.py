#from turtle import title
# from xml.dom.minidom import AttributeList
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist_list = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    favorite = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def check_is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self:
                return True


# class Artist(models.Model):
#     artist = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)


# class User(AbstractUser):
#     pass


class Favorite(models.Model):
    #user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='favorites', null=True, blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='favorites', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}:{self.album}'
