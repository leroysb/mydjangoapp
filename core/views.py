from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# from .forms import CommentForm
from .models import *
import datetime

# Create your views here.

def page404 (request, exception):
    return render(request, 'core/404.html')

# def page500 (request, exception):
#     return render(request, 'core/500.html')

class AboutView(TemplateView):
    template_name = 'core/about.html'

class HomepageView(ListView):
    template_name = 'core/homepage.html'
    queryset = Article.objects.first()

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.order_by('-publishdate')[0:4]
        context['gigs'] = Event.objects.filter(date__gte = datetime.date.today()).order_by('-date')
        context['podcast'] = Podcast.objects.first()
        context['episodes'] = PodcastEpisode.objects.order_by('-pubDate')[0:2]
        return context

class BlogView(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-publishdate')
    template_name = 'core/blog.html'

class ArticleView(DetailView):
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
    context_object_name = 'event'
    queryset = Event.objects.filter(date__lte = datetime.date.today()).order_by('-date')
    template_name = 'core/events.html'

class PrivacyView(ListView):
    context_object_name = 'privacy'
    queryset = Privacy.objects.order_by('-date').first()
    template_name = 'core/privacy.html'

class TermsView(ListView):
    context_object_name = 'terms'
    queryset = Terms.objects.order_by('-date').first()
    template_name = 'core/terms.html'