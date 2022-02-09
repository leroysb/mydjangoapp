# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy, reverse
# from django.http import HttpResponseForbidden, HttpResponseRedirect
# # from django.http.response import HttpResponseNotFound

# from django.db.models import F

# from django.views import View
# from django.views.generic import ListView, DetailView, TemplateView, FormView
# from django.views.generic.edit import FormMixin, ModelFormMixin
# from django.views.generic.detail import SingleObjectMixin
# # from django.views.generic.list import MultipleObjectMixin

# # from django.core.paginator import Paginator, InvalidPage

# # from urllib import quote_plus
# from .models import *
# from .forms import *
# import datetime

# # Error views.

# def page404 (request, exception):
#     return render(request, 'core/404.html')

# def page500 (request):
#     return render(request, 'core/serverError.html')

# # Page views.

# class HomepageView(TemplateView):
#     template_name = 'core/homepage.html'

# class BlogView(ListView):
#     context_object_name = 'articles'
#     queryset = Article.objects.order_by('-publishdate')
#     template_name = 'core/blog.html'

# class ArticleView(FormMixin, DetailView):
#     model = Article
#     context_object_name = 'article'
#     template_name = 'core/articlelayout.html'
#     success_url = 'core:blogpost'
#     form_class = commentForm

#     def post(self, request, *args, **kwargs):

#         if 'submitcomment' in request.POST:
#             form = commentForm(request.POST)
#             if form.is_valid():
#                 post = self.get_object()
#                 form.instance.name = request.user
#                 form.instance.post = post
#                 form.save()
#                 return redirect(reverse('core:blogpost', kwargs={'pk':post.id, 'slug':post.slug}))
#         else:
#             form = feedbackForm(request.POST)
#             if form.is_valid():
#                 post = self.get_object()
#                 form.instance.source = post
#                 form.save()
#                 return redirect(reverse('core:blogpost', kwargs={'pk':post.id, 'slug':post.slug}))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'form': self.form_class,
#             # 'share_string': quote_plus(self.object.extract),
#         })
#         return context

#     # def get_object(self):
#     #     obj = super().get_object()
#     #     context = {}
#     #     Article.objects.filter(pk=obj.pk).update(visits=F('visits') + 1)
#     #     visits = Article.objects.filter(pk=obj.pk).get('visits')
#     #     context['visits'] = visits.views += 1   
#     #     return context

#     def get(self, request, *args, **kwargs):
#             self.object = self.get_object()
#             context = self.get_context_data(object=self.object)
#             ip = get_client_ip(self.request)

#             post_details=Article.objects.get(pk=self.object.pk)
#             # if not ArticleStat.objects.filter(IPAddres=ip, article=post_details).exists():
#             ArticleStat.objects.get_or_create(
#                 article=post_details,
#                 IPAddres=ip,
#                 device =request.META.get('HTTP_USER_AGENT'),)
#             return self.render_to_response(context)

# class PodcastView(ListView):
#     context_object_name = 'podcast'
#     queryset = Podcast.objects.first()
#     template_name = 'core/podcastLayout.html'

# class EpisodeView(DetailView):
#     model = PodcastEpisode
#     context_object_name = 'episode'
#     template_name = 'core/episode.html'

# class EventList(ListView):
#     context_object_name = 'events'
#     queryset = Event.objects.filter(date__lte = datetime.date.today()).order_by('-date')
#     template_name = 'core/events.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['gigs'] = Event.objects.filter(date__gte = datetime.date.today()).order_by('-date')
#         return context

# class LegalView(ListView):
#     context_object_name = 'privacy'
#     queryset = Privacy.objects.order_by('-date').first()
#     template_name = 'core/legal.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['terms'] = Terms.objects.order_by('-date').first()
#         return context

# def get_client_ip(request):
#     ipaddress = request.META.get('HTTP_X_FORWARDED_FOR')
#     if ipaddress:
#         ip = ipaddress.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip