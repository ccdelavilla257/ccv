from django.urls import path
from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.gallery_index, name="index"),
    path("album/<int:album_id>/", views.album_detail, name="album_detail"),
]
