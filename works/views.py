from django.shortcuts import render, get_object_or_404
from django.views import View
from works.models import Album


class WorksView(View):
    def get(self, request):
        works = Album.objects.filter(is_active=True)

        context = {
            'works': works,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('works/works.html'), context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)
        
        context = {
            'album': album,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('works/album.html'), context)