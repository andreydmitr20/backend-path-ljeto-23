from django.urls import path
from . import views

app_name = "music_store"

urlpatterns = [
    path("bands/", views.band_listing, name="band-list"),
    path("", views.home_page, name="home-page"),
    path("bands/<int:band_id>/", views.band_detail, name="band-detail"),
    path("bands/search", views.band_search, name="band-search"),
]
