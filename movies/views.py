import requests
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    # Lista ampliada de IDs de filmes populares para testar paginação
    popular_ids = [
        "tt1375666",
        "tt0133093",
        "tt0816692",
        "tt0120737",
        "tt0111161",
        "tt0109830",
        "tt0076759",
        "tt0167260",
        "tt0468569",
        "tt0050083",
        "tt0108052",
        "tt0120689",
        "tt0068646",
        "tt0137523",
        "tt0110912",
    ]

    popular_movies = []
    for imdb_id in popular_ids:
        response = requests.get(
            f"http://www.omdbapi.com/?i={imdb_id}&apikey={settings.OMDB_API_KEY}"
        )
        if response.status_code == 200:
            popular_movies.append(response.json())

    # Paginação com 6 itens por página
    paginator = Paginator(popular_movies, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})


@require_GET
def movie_detail(request, imdb_id):
    response = requests.get(
        f"http://www.omdbapi.com/?i={imdb_id}&apikey={settings.OMDB_API_KEY}"
    )
    movie = response.json() if response.status_code == 200 else None

    # Filmes similares (baseado no gênero)
    similar_movies = []
    if movie:
        genre = movie.get("Genre", "").split(",")[0]
        search_response = requests.get(
            f"http://www.omdbapi.com/?s={genre}&type=movie&apikey={settings.OMDB_API_KEY}"
        )
        if search_response.status_code == 200:
            similar_movies = search_response.json().get("Search", [])[:4]

    return render(
        request, "movie_detail.html", {"movie": movie, "similar_movies": similar_movies}
    )


@require_GET
def search_results(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        response = requests.get(
            f"http://www.omdbapi.com/?s={query}&apikey={settings.OMDB_API_KEY}"
        )
        if response.status_code == 200:
            results = response.json().get("Search", [])

    return render(request, "search_results.html", {"results": results, "query": query})
