from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("id","name", "location")
admin.site.register(Event, EventAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("id","name")
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("id","name")
admin.site.register(ArticleTag, ArticleTagAdmin)

class ArticleStatAdmin(admin.ModelAdmin):
    list_display = ("IPAddres","article","visited")
    readonly_fields = ('IPAddres', 'article', 'device', 'visited')
admin.site.register(ArticleStat, ArticleStatAdmin)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ("id", "title", "category", "publishdate")
admin.site.register(Article, ArticleAdmin)

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ("id","content_type","content")
    readonly_fields = ('user', 'content', 'timestamp')
admin.site.register(ArticleComment, ArticleCommentAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id","postdate","content","ratings")
    readonly_fields = ("postdate","content","ratings","source")
admin.site.register(Feedback, FeedbackAdmin)

class TermsAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Terms, TermsAdmin)

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Privacy, PrivacyAdmin)