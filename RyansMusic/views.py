from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm
from django.shortcuts import get_object_or_404


def list_albums(request):
    albums = Album.objects.all()

    return render(request, "RyansMusic/list_albums.html", 
                    {"albums": albums})


def album_detail(request, pk):
    albums = get_object_or_404(Album, pk=pk)

    return render(request, "RyansMusic/album_detail.html", 
                    {"albums": albums})


def add_album(request):
    if request.method == "GET":
        forms = AlbumForm()
    else:
        forms = AlbumForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(to="list_albums")

    return render(request, "RyansMusic/add_album.html", 
                    {"forms": forms})


def delete_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        albums.delete()
        return redirect(to="list_albums")
    return render(request, "RyansMusic/delete_album.html", 
                    {"albums": albums})


def edit_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        forms = AlbumForm(instance=albums)

    else:
        forms = AlbumForm(data=request.POST, instance=albums)
        if forms.is_valid():
            forms.save()
            return redirect(to="list_albums")

    return render(request, "RyansMusic/edit_album.html", 
                    {"forms": forms, "albums": albums})


