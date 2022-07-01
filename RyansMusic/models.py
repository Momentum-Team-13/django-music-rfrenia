# from turtle import title
# from xml.dom.minidom import AttributeList
from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    artist_list = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)


# class Artist(models.Model):
#     album = models.ManyToManyField("Album", null=True, blank=True)

#     def __str__(self):
#         return f'{self.artist}'
