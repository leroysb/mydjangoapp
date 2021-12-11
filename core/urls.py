from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("privacy-policy", PrivacyView.as_view(), name="privacy"),
    path("terms-of-use", TermsView.as_view(), name="terms"),
    # path('events', EventList.as_view(), name="events"),
    path('kubonga-show', PodcastView.as_view(), name="podcast"),
    path("a-z-logs", BlogView.as_view(), name="blogpage"),
    path("blog", BlogView.as_view(), name="blogpage"),
    path("a-z-logs/entry-<int:pk>", ArticleView.as_view(), name="blogpost"),
    path("kubonga-show/episode-<int:pk>", EpisodeView.as_view(), name="episode"),
]