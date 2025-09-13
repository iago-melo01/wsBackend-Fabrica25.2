from django.shortcuts import render
from django.conf import settings
from django import http
from django import http
import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from .models import Movie
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("TMDB_API_KEY")

def home_view(request):
    return render(request, 'home.html')

def buscar_filmes_view(request):
    pesquisa = request.GET.get("q") #query passada no form de busca
    page = int(request.GET.get("page", 1))
    params = {
        "api_key": API_KEY,# ta exposta mas jaja eu boto no .env
        "language": "pt-BR",
        "query": pesquisa,
        "page": page,
        "include_adult": "false",
        "region": "BR",
                 }
    r = requests.get('https://api.themoviedb.org/3/search/movie', params=params, timeout=10)
    dados = r.json() #armazena a resposta json da requisicao na variavel dados
    
    resultados = dados.get("results")
    return render(request, 'resultados.html', {'resultados': resultados, 'query': pesquisa})

def visualizar_filme(request, movieId):
    if not movieId: #se movieId nao for passado, retornar HttpBadRequest
        return http.HttpResponseBadRequest("Parâmetro 'external_id' é obrigatório.")
    
    url = f"https://api.themoviedb.org/3/movie/{movieId}"

    params = {
        "api_key": API_KEY,   
        "language": 'pt-BR', 
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        return http.HttpResponseServerError(f"Erro ao contatar TMDb: {e}")

    dados = resp.json()
    print(dados)
    
    return render(request, 'visualizacao_filme.html', {"filme": dados})