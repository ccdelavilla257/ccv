from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("buscar/", views.blog_search, name="buscar"),
    path("<int:pk>/", views.post_detail, name="detail"),  # <-- CAMBIA AQUÍ (slug → pk)
]
