from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Privacy, Terms

class PodcastView(TemplateView):
    template_name = 'core/podcast.html'

class LegalView(ListView):
    context_object_name = 'privacy'
    queryset = Privacy.objects.order_by('-date')
    template_name = 'core/legal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms'] = Terms.objects.order_by('-date')
        return context