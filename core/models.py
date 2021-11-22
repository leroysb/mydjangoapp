from django.core.files import storage
from django.db import models
from django.db.models.deletion import *
from django.core.files.storage import FileSystemStorage
from account.models import User
from ckeditor.fields import RichTextField

# Create your models here. 

class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article_category'

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    featureimage = models.ImageField(upload_to='core/article/%Y/%m/')
    title = models.CharField(max_length = 500)
    # tag = models.CharField(max_length=255, blank=True, null=True, default= 'untagged')
    category = models.ForeignKey(ArticleCategory, related_name="articles", on_delete=models.PROTECT,)
    writer = models.CharField(max_length=100, default = 'Leroy Buliro')
    credit = models.CharField(max_length = 700, blank=True, null=True)
    publishdate = models.DateField(auto_now_add=False)
    extract = models.CharField(max_length = 2000, blank=True, null=True)
    content = RichTextField(config_name='full_editor', blank=True, null=True)

    def __str__(self):
        return f"Adding {self.title} by {self.writer}"

    class Meta:
        db_table = 'article'

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    poster = models.ImageField(upload_to='core/events/%Y/%m/')
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]
        db_table = 'event'

class mailinglist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mailinglist'


class Podcast(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='core/podcast/')
    title = models.CharField(max_length = 255, unique=True)
    description = RichTextField(config_name='full_editor', blank=True, null=True)
    appleurl = models.URLField(max_length = 255, unique=True)
    googleurl = models.URLField(max_length = 255, unique=True)
    spotifyurl = models.URLField(max_length = 255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'podcast'

class PodcastEpisode(models.Model):
    id = models.BigAutoField(primary_key=True)
    podcast = models.ForeignKey(Podcast, related_name="episodes", on_delete=models.CASCADE)
    season = models.IntegerField()
    episode = models.IntegerField()
    title = models.CharField(max_length = 500)
    image = models.ImageField(upload_to='core/podcast/')
    summary = models.CharField(max_length = 500)
    description = RichTextField(config_name='full_editor', blank=True, null=True)
    audio = models.FileField(upload_to='core/podcast/')
    pubDate = models.DateField(auto_now_add=False)

    class Meta:
        ordering = ["-episode"]
        db_table = 'podcast_episode'

class Terms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

class Privacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

#class tagdb(models.Model):
    #id = models.AutoField(primary_key=True)
    #article = models.ForeignKey(blogdb, on_delete=models.CASCADE, related_name="tags", related_query_name="tag",)
    #name = models.CharField(max_length=255)

# class ArticleComment(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     postdate = models.DateTimeField(auto_now_add=True)
#     body = models.TextField(max_length=400, blank=False)

#     class Meta:
#             db_table = 'article_comment'