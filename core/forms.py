from django import forms
from django.forms import Form, ModelForm

from core.models import Feedback

class CommentForm(Form):
    comment = forms.CharField (min_length=1, max_length=400)

class feedbackForm(ModelForm):
    content = forms.CharField (min_length=1, max_length=500)
    ratings = forms.RadioSelect()
    # source = forms.CharField (min_length=1, max_length=500)

    class Meta:
        model = Feedback
        fields = ['content', 'ratings',]