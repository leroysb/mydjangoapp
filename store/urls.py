from django.urls import path
from .views import CatalogueView

app_name = "store"

urlpatterns = [
    path("", CatalogueView.as_view(), name="catalogue"),
]