from cgitb import lookup
from pdb import post_mortem
from re import I
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
# from django.http.response import HttpResponseNotFound
from django.views.generic.edit import FormMixin
from pkg_resources import get_importer
# from django.views.generic.list import MultipleObjectMixin
# from django.core.paginator import Paginator, InvalidPage

from .models import *
from .forms import *
import datetime

# Error views.

def page404 (request, exception):
    return render(request, 'core/404.html')

def page500 (request):
    return render(request, 'core/serverError.html')

# Page views.

class HomepageView(TemplateView):
    template_name = 'core/homepage.html'

class BlogView(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-publishdate')
    template_name = 'core/blog.html'

class ArticleView(FormMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'core/articlelayout.html'
    form_class = feedbackForm

    def get_success_url(self):
        return reverse("core:blogpost", kwargs={"slug": self.object.slug, "pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if Stat.objects.filter(ip=ip).exists():
            print("ip already exists")
            article_id = request.GET.get('article-id')
            print(article_id)
            post = Article.objects.get(pk=article_id)
            post.views.add(Stat.objects.get(ip=ip))
        else:
            Stat.objects.create(ip=ip)
            article_id =request.GET.get('article-id')
            post = Article.objects.get(pk=article_id)
            post.views.add(Stat.objects.get(ip=ip))
        return self.render_to_response(context)

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

def get_client_ip(request):
    ipaddress = request.META.get('HTTP_X_FORWARDED_FOR')
    if ipaddress:
        ip = ipaddress.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

    