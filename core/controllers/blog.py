from django import forms
from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from core.models import Feedback, ArticleComment
from ..models import *
from ..utils import get_client_ip

class commentForm(forms.ModelForm):
    comment = forms.CharField(min_length=1, max_length=420, widget=forms.Textarea(attrs={'rows':4}) )
    
    class Meta:
        model = ArticleComment
        fields = ['comment',]

class feedbackForm(forms.ModelForm):
    content = forms.CharField (min_length=1, max_length=500)
    ratings = forms.RadioSelect()

    class Meta:
        model = Feedback
        fields = ['content', 'ratings',]

def BlogView(request, *args, **kwargs):
    context = {}
    context['articles'] = Article.objects.order_by('-publishdate')

    if 'submitfeedback' in request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid(): 
            form.instance.source = 'blog home'
            form.save()
            return redirect(reverse('core:blog'))

    return render(request, 'core/blog.html', context)

class ArticleView(FormMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'core/articlelayout.html'
    success_url = 'core:blogpost'
    form_class = commentForm

    def post(self, request, *args, **kwargs):

        if 'submitcomment' in request.POST:
            form = commentForm(request.POST)
            if form.is_valid():
                post = self.get_object()
                form.instance.name = request.user
                form.instance.post = post
                form.save()
                return redirect(reverse('core:blogpost', kwargs={'pk':post.id, 'slug':post.slug}))
        else:
            form = feedbackForm(request.POST)
            if form.is_valid():
                post = self.get_object()
                form.instance.source = post
                form.save()
                return redirect(reverse('core:blogpost', kwargs={'pk':post.id, 'slug':post.slug}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form_class,
            # 'share_string': quote_plus(self.object.extract),
        })
        return context

    def get(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            ip = get_client_ip(self.request)

            post_details=Article.objects.get(pk=self.object.pk)
            # if not ArticleStat.objects.filter(IPAddres=ip, article=post_details).exists():
            ArticleStat.objects.get_or_create(
                article=post_details,
                IPAddres=ip,
                device =request.META.get('HTTP_USER_AGENT'),)
            return self.render_to_response(context)