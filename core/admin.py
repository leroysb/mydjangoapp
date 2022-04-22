from django.contrib import admin
from .models import *

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