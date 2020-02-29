from django.shortcuts import render, get_object_or_404
from django.views import View
from works.models import Album


class WorksView(View):
    def get(self, request):
        works = Album.objects.filter(is_active=True)

        context = {
            'works': works,
        }
        return render(request, 'works/works.html', context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)
        
        context = {
            'album': album,
        }
        return render(request, 'works/album.html', context)
