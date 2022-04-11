from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("kubonga-show", PodcastView.as_view(), name="podcast"),
    path("legal", LegalView.as_view(), name="legal"),
]