from django.shortcuts import render, get_object_or_404
from django.views import View
from news.models import News


class NewsView(View):
    def get(self, request):
        news = News.objects.filter(is_active=True)

        context = {
            'news': news,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('news/news.html'), context)


class NewsDetailView(View):
    def get(self, request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)

        context = {
            'news_item': news_item,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('news/news_detail.html'), context)