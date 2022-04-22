from django.urls import path
from .views import LegalView, PodcastView
from .controllers.homepage import HomepageView

app_name = "core"

urlpatterns = [
    path("", HomepageView, name="index"),
    path("kubonga-show/", PodcastView.as_view(), name="podcast"),
    path("legal/", LegalView.as_view(), name="legal"),
]