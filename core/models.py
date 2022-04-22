from django.db import models
from django.db.models.deletion import *
from ckeditor.fields import RichTextField

class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    postdate = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=False)
    ratings = models.IntegerField()
    source = models.CharField(max_length = 200, blank=False)

    class Meta:
        ordering = ["-postdate"]
        db_table = 'feedback'

class Terms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

class Privacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)