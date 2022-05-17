from audioop import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
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
        ordering = ['-date']
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
    IPAddres= models.GenericIPAddressField(default='0.0.0.0')
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    # session = models.CharField(max_length=40, null=True)
    device = models.CharField(max_length=400 ,default='null')
    visited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} in {1} article'.format(self.IPAddres,self.article.title)

    class Meta:
        ordering = ['-visited']
        db_table = 'article_stat'

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    featureimage = models.ImageField(upload_to='core/article/%Y/%m/')
    featureimageURI = models.URLField()
    title = models.CharField(max_length = 500)
    slug = models.CharField(max_length = 500)
    tags = models.ManyToManyField(ArticleTag, related_name='tags')
    category = models.ForeignKey(ArticleCategory, related_name='articles', on_delete=models.PROTECT)
    writer = models.CharField(max_length=100, default = 'Leroy Buliro')
    credit = models.CharField(max_length = 700, blank=True, null=True)
    publishdate = models.DateField(auto_now_add=False)
    extract = models.CharField(max_length = 2000, blank=True, null=True)
    content = RichTextField(config_name='full_editor', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    @property
    def viewsCount(self):
        return ArticleStat.objects.filter(article=self).count()

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishdate']
        db_table = 'article'

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT) 
    content = models.TextField(max_length=420, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']
        db_table = 'comments'

    def replies(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    postdate = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=False)
    ratings = models.IntegerField()
    source = models.CharField(max_length = 200, blank=False)

    class Meta:
        ordering = ['-postdate']
        db_table = 'feedback'

class Terms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)

class Privacy(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    content = RichTextField(config_name='full_editor', blank=False, null=False)