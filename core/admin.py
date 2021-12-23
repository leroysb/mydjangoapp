from django.contrib import admin
from .models import *

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("id","name")
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ("id", "title", "category", "publishdate")
admin.site.register(Article, ArticleAdmin)

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ("id","post","content")
admin.site.register(ArticleComment, ArticleCommentAdmin)

class PodcastAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',),}
    list_display = ("id","title",)
admin.site.register(Podcast, PodcastAdmin)

class PodcastEpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ("podcast", "season", "episode", "title",)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("id","name", "location")
admin.site.register(Event, EventAdmin)

class TermsAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Terms, TermsAdmin)

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("id","date", "content")
admin.site.register(Privacy, PrivacyAdmin)