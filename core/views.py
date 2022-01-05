from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator, InvalidPage

# from .forms import CommentForm
from .models import *
import datetime

# Create your views here.

def page404 (request, exception):
    return render(request, 'core/404.html')

# def page500 (request, exception):
#     return render(request, 'core/500.html')

class HomepageView(TemplateView):
    template_name = 'core/homepage.html'

class BlogView(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-publishdate')
    template_name = 'core/blog.html'

class ArticleView(DetailView):
    context_object_name = 'article'
    model = Article
    template_name = 'core/articlelayout.html'

class PodcastView(ListView):
    context_object_name = 'podcast'
    queryset = Podcast.objects.first()
    template_name = 'core/podcast.html'

class EpisodeView(DetailView):
    model = PodcastEpisode
    context_object_name = 'episode'
    template_name = 'core/episode.html'

class EventList(ListView):
    context_object_name = 'events'
    queryset = Event.objects.filter(date__lte = datetime.date.today()).order_by('-date')
    template_name = 'core/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gigs'] = Event.objects.filter(date__gte = datetime.date.today()).order_by('-date')
        return context

class LegalView(ListView):
    context_object_name = 'privacy'
    queryset = Privacy.objects.order_by('-date').first()
    template_name = 'core/legal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms'] = Terms.objects.order_by('-date').first()
        return context