from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    # path("legal", LegalView.as_view(), name="legal"),
]