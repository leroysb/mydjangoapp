from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("a-z-logs", BlogView.as_view(), name="blogpage"),
    path("a-z-logs/entry-<int:pk>/<slug:slug>", ArticleView.as_view(), name="blogpost"),
    path('kubonga-show', PodcastView.as_view(), name="podcast"),
    path("kubonga-show/s<int:s>e<int:e>/<slug:slug>", EpisodeView.as_view(), name="episode"),
    path("legal", LegalView.as_view(), name="legal"),
    path('events', EventList.as_view(), name="event"),
]