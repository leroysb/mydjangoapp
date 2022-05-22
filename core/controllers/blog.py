from django import forms
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from core.models import Feedback, Comment, Article, ArticleStat
from ..utils import get_client_ip

class commentForm(forms.Form):
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':4, 
            'placeholder': 'This conversation is moderated.'
        }), 
        min_length=1, 
        max_length=420
    )

    # class Meta:
    #     model = Feedback
    #     fields = ['content_type', 'object_id', 'parent_id', 'content']

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
    obj = get_object_or_404(Article, pk=pk, slug=slug)
    context['article'] = obj

    ip = get_client_ip(request)
    post_details=Article.objects.get(pk=obj.pk)
    ArticleStat.objects.get_or_create(
        article=post_details,
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    
    form = commentForm(request.POST or None)
    context['form'] = form
    if 'submitcomment' in request.POST:
        if form.is_valid():
            user = request.user
            content = form.cleaned_data.get('content')
            content_type = obj.get_content_type
            # content_type = ContentType.objects.get(model=c_type)
            object_id = obj.pk
            parent = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(pk=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent = parent_qs.first()

            Comment.objects.get_or_create(
                user = user,
                content_type = content_type,
                object_id = object_id,
                content = content, 
                parent = parent
            )
            
            return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    if 'deletecomment' in request.POST:
        instance = get_object_or_404(Comment, pk=id)
        instance.delete()
        return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    # if 'submitfeedback' in request.POST:
    #     form = feedbackForm(request.POST)
    #     if form.is_valid():
    #         form.instance.source = obj
    #         form.save()

    return render(request, 'core/articlelayout.html', context)
    