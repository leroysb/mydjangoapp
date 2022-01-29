from colorsys import ONE_SIXTH
from django.db import models
from django.db.models.deletion import *
from account.models import User
from ckeditor.fields import RichTextField
# from django.core.files import storage
# from django.core.files.storage import FileSystemStorage

import datetime

# Create your models here. 

class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article_category'

class ArticleTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article_tag'

class ArticleStat(models.Model):
    IPAddres= models.GenericIPAddressField(default="0.0.0.0")
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    session = models.CharField(max_length=40)
    device = models.CharField(max_length=400 ,default='null')
    created = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return '{0} in {1} article'.format(self.IPAddres,self.article.title)

    class Meta:
        ordering = ["-created"]
        db_table = 'article_stat'

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    featureimage = models.ImageField(upload_to='core/article/%Y/%m/')
    title = models.CharField(max_length = 500)
    slug = models.CharField(max_length = 500,)
    tags = models.ManyToManyField(ArticleTag, related_name="tags")
    category = models.ForeignKey(ArticleCategory, related_name="articles", on_delete=models.PROTECT,)
    writer = models.CharField(max_length=100, default = 'Leroy Buliro')
    credit = models.CharField(max_length = 700, blank=True, null=True)
    publishdate = models.DateField(auto_now_add=False)
    extract = models.CharField(max_length = 2000, blank=True, null=True)
    content = RichTextField(config_name='full_editor', blank=True, null=True)
    # visits = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    @property
    def viewsCount(self):
        return ArticleStat.objects.filter(article=self).count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publishdate"]
        db_table = 'article'

class ArticleComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    postdate = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=420, blank=False)

    class Meta:
        ordering = ["-postdate"]
        db_table = 'article_comment'

class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    postdate = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=False)
    ratings = models.IntegerField()
    source = models.CharField(max_length = 200, blank=False)

    class Meta:
        ordering = ["-postdate"]
        db_table = 'feedback'

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
    slug = models.CharField(max_length = 500)
    tags = models.CharField(max_length=500, default= 'untagged')
    image = models.ImageField(upload_to='core/podcast/')
    summary = models.CharField(max_length = 500)
    description = RichTextField(config_name='full_editor', blank=True, null=True)
    audio = models.FileField(upload_to='core/podcast/')
    pubDate = models.DateField(auto_now_add=False)

    class Meta:
        ordering = ["-episode"]
        db_table = 'podcast_episode'

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length = 500)
    location = models.CharField(max_length=100, blank=False)
    poster = models.ImageField(upload_to='core/events/%Y/%m/')
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]
        db_table = 'event'

class Terms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

class Privacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)