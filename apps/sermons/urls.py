from django.urls import path
from . import views

app_name = "sermons"

urlpatterns = [
    path("", views.sermon_list, name="list"),
    path("buscar/", views.sermon_search, name="buscar"),
    path("ano/<int:year>/", views.sermons_by_year, name="by_year"),
    path("<int:pk>/", views.sermon_detail, name="detail"),
]
