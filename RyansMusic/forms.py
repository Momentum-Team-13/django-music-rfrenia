from django import forms
from .models import Album
#from .models import Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist_list',
            'created_at',
        ]