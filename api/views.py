from django.shortcuts import render
from django.conf import settings
from django import http
import requests
from .models import Movie
# Create your views here.
BASE_URL = "https://www.omdbapi.com/"

def fetch_by_title(request):
    
    params = { "apikey": '1ab60fb9', "plot": "full", "s": request.GET.get("q")}
    r = requests.get(BASE_URL, params=params, timeout=10)
    dados = r.json()
    resultados = dados.get("Search", [])
    return render(request, 'resultados.html', {'resultados': resultados})

def buscar_filmes_view(request):
    pesquisa = request.GET.get("q")
    page = int(request.GET.get("page", 1))
    params = {
        "api_key": '6c44618ae8b3b5700c325cc765462c96',
        "language": "pt-BR",
        "query": pesquisa,
        "page": page,
        "include_adult": "false",
        "region": "BR",
                 }
    r = requests.get('https://api.themoviedb.org/3/search/movie', params=params, timeout=10)
    dados = r.json()
    resultados = dados.get("results")
    return render(request, 'resultados.html', {'resultados': resultados})

def home_view(request):
    return render(request, 'home.html')