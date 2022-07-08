from django.shortcuts import render, redirect
from .models import Album, Favorite
from .forms import AlbumForm, FavoriteForm
from django.shortcuts import get_object_or_404


def list_albums(request):
    albums = Album.objects.all()
    favorite_albums = [album for album in albums if album.check_is_user_favorite(request.user)]
    return render(request, "RyansMusic/list_albums.html", 
                    {"albums":albums, "favorite_albums":favorite_albums})


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


def add_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = FavoriteForm
    else:
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "RyansMusic/add_favorite.html", {"form":form, "album":album})


def delete_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk) 
    favorite = album.favorites.get()
    if request.method == 'GET':
        return render(request, "RyansMusic/delete_favorite.html", {"album":album, "pk":pk})
    if request.method == 'POST':
        favorite.delete()
        return redirect(to='list_albums')
    return render(request, "RyansMusic/delete_favorite.html", {"album":album})


