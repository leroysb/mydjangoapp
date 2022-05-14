from django import forms
from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from core.models import Feedback
# from core.models import Feedback, ArticleComment
from ..models import *
from ..utils import get_client_ip

# class commentForm(forms.ModelForm):
#     comment = forms.CharField(min_length=1, max_length=420, widget=forms.Textarea(attrs={'rows':4}) )
    
#     class Meta:
#         model = ArticleComment
#         fields = ['comment',]

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

def ArticleView(request, pk, slug):
    context = {}
    obj = Article.objects.get(pk=pk)
    context['article'] = obj
    context['form'] = feedbackForm()
    
    # if 'submitcomment' in request.POST:
    #     form = commentForm(request.POST)
    #     if form.is_valid():
    #         post = obj
    #         form.instance.name = request.user
    #         form.instance.post = post
    #         form.save()
    
    if 'submitfeedback' in request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.instance.source = obj
            form.save()
            

    ip = get_client_ip(request)
    post_details=Article.objects.get(pk=obj.pk)
    ArticleStat.objects.get_or_create(article=post_details, IPAddres=ip, device =request.META.get('HTTP_USER_AGENT'))

    return render(request, 'core/articlelayout.html', context)