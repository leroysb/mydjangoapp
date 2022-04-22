from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django import forms
from django.forms import Form, ModelForm
from core.models import Feedback

class feedbackForm(ModelForm):
    content = forms.CharField (min_length=1, max_length=500)
    ratings = forms.RadioSelect()

    class Meta:
        model = Feedback
        fields = ['content', 'ratings',]

def HomepageView(request):
    context = {}
    context['form'] = feedbackForm()

    if request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.instance.source = "homepage"
            form.save()

    return render(request, 'core/homepage.html', context)