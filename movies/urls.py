from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search_results, name="search_results"),
    path("movie/<str:imdb_id>/", views.movie_detail, name="movie_detail"),
]
