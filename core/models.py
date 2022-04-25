from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import *
from ckeditor.fields import RichTextField

User = get_user_model()

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length = 500)
    location = models.CharField(max_length=100, blank=False)
    poster = models.ImageField(upload_to='core/events/%Y/%m/')
    posterURI = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]
        db_table = 'event'

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
    # session = models.CharField(max_length=40, null=True)
    device = models.CharField(max_length=400 ,default='null')
    # created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{0} in {1} article'.format(self.IPAddres,self.article.title)

    class Meta:
        # ordering = ["-created"]
        db_table = 'article_stat'

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    featureimage = models.ImageField(upload_to='core/article/%Y/%m/')
    featureimageURI = models.URLField()
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

class Terms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

class Privacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)