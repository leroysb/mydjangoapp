from django.urls import path
from .views import LegalView, PodcastView
from .controllers.homepage import HomepageView
from .controllers.blog import BlogView, ArticleView
from .controllers.events import EventView

app_name = "core"

urlpatterns = [
    path("", HomepageView, name="index"),
    path("events/", EventView.as_view(), name="events"),
    path("a-z-logs/", BlogView.as_view(), name="blog"),
    path("a-z-logs/entry-<int:pk>/<slug:slug>/", ArticleView.as_view(), name="article"),
    path("kubonga-show/", PodcastView.as_view(), name="podcast"),
    path("legal/", LegalView.as_view(), name="legal"),
]