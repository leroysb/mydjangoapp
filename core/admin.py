from django.contrib import admin
from .models import *

class mailinglistAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
admin.site.register(mailinglist, mailinglistAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "writer", "publishdate")
admin.site.register(Article, ArticleAdmin)

# class ArticleCommentAdmin(admin.ModelAdmin):
#     list_display = ("id","post","body")
# admin.site.register(ArticleComment, ArticleCommentAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ("id","name", "location")
admin.site.register(Event, EventAdmin)

class PodcastAdmin(admin.ModelAdmin):
    list_display = ("id","image","title", "description","appleurl", "googleurl","spotifyurl")
admin.site.register(Podcast, PodcastAdmin)

class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast", "season", "episode", "title", "image", "summary", "description","audio", "pubDate")
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)

class TermsAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Terms, TermsAdmin)

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Privacy, PrivacyAdmin)