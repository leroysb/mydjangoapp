from django.urls import path
from .views import CatalogueView

app_name = "store"

urlpatterns = [
    path("shop/", CatalogueView.as_view(), name="shop"),
]