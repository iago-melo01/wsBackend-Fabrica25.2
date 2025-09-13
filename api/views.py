from django.shortcuts import render
from django.conf import settings
from django import http
from django import http
import requests
from .models import Movie

def buscar_filmes_view(request):
    pesquisa = request.GET.get("q") #query 
    page = int(request.GET.get("page", 1))
    params = {
        "api_key": 'a909fa9b7f3a8af856687641b53cde62',
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

def visualizar_filme(request, movieId):

    
    
    if not movieId:
        return http.HttpResponseBadRequest("Parâmetro 'external_id' é obrigatório.")
    
    url = f"https://api.themoviedb.org/3/movie/{movieId}"

    params = {
        "api_key": 'a909fa9b7f3a8af856687641b53cde62',   # V3 → na query string
        #"external_source": 'imdb_id',
        "language": 'pt-BR',
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        return http.HttpResponseServerError(f"Erro ao contatar TMDb: {e}")

    dados = resp.json()
    print(dados)
    
    return render(request, 'visualizacao_filme.html', {"filme": dados})