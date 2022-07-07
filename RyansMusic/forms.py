from django import forms
from .models import Album, Favorite
#from .models import Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist_list',
        ]

# class ArtistForm(forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = [
#             'artist',
#             'name',
#         ]

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            #'user',
            'album',
        ]