from django import forms
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from core.models import Feedback, Comment, Article, ArticleStat
from ..utils import get_client_ip

class commentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))

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
    obj = get_object_or_404(Article, pk=pk)
    context['article'] = obj
    context['form'] = commentForm()
    context['commentsCount'] = Comment.objects.filter(content_type=obj.get_content_type, object_id=obj.id).count()

    ip = get_client_ip(request)
    post_details=Article.objects.get(pk=obj.pk)
    ArticleStat.objects.get_or_create(
        article=post_details,
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )

    initial_data = {
        "content_type": obj.get_content_type,
        "object_id": obj.id,
    }
    
    if 'submitcomment' in request.POST:
        form = commentForm(request.POST, initial=initial_data)
        if form.is_valid():
            content = form.cleaned_data['content']
            object_id = form.cleaned_data['object_id']
            c_type = form.cleaned_data['content_type']
            content_type = ContentType.objects.get(model=c_type)
            parent = None

            try:
                parent_id = request.POST.get('parent_id')
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(pk=parent_id)
                if parent_qs.exists():
                    parent = parent_qs.first()

            new_comment = Comment(
                user = request.user,
                content_type = content_type,
                object_id = object_id,
                parent = parent,
                content = content,
            )
            new_comment.save(force_insert=True)
            return redirect(reverse('core:article', kwargs={'pk':obj.id}))
    
    # if 'submitfeedback' in request.POST:
    #     form = feedbackForm(request.POST)
    #     if form.is_valid():
    #         form.instance.source = obj
    #         form.save()

    return render(request, 'core/articlelayout.html', context)
    