from django import forms
from django.forms import Form, ModelForm
from core.models import Feedback, ArticleComment

class commentForm(ModelForm):
    comment = forms.CharField(min_length=1, max_length=420, widget=forms.Textarea(attrs={'rows':4}) )
    
    class Meta:
        model = ArticleComment
        fields = ['comment',]

class feedbackForm(ModelForm):
    content = forms.CharField (min_length=1, max_length=500)
    ratings = forms.RadioSelect()

    class Meta:
        model = Feedback
        fields = ['content', 'ratings',]