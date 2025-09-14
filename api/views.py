from django.shortcuts import render
from django.conf import settings
from django import http
from django.shortcuts import get_object_or_404, redirect
import requests
from django.urls import reverse 
from pathlib import Path
import os
from dotenv import load_dotenv
from .models import FilmeAvaliado, Avaliacao
from datetime import datetime
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("TMDB_API_KEY")

def home_view(request):
    return render(request, 'home.html')

def buscar_filmes_view(request):
    pesquisa = request.GET.get("q") #query passada no form de busca
    page = int(request.GET.get("page", 1))
    params = {
        "api_key": API_KEY, #nao esta mais exposta
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

    filme = get_object_or_404(FilmeAvaliado, imdbID=movieId)
    comentarios = (Avaliacao.objects.filter(filme=filme))

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
    
    return render(request, 'visualizacao_filme.html', {"filme": dados, "comentarios": comentarios})

def criar_avaliacao(request, movieId):
    if request.method == "POST":
        nota = request.POST.get("nota")
        comentario = request.POST.get("texto")


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

        release_str = dados.get("release_date") or ""
        release_date = None
        if release_str:
            try:
                release_date = datetime.strptime(release_str, "%Y-%m-%d").date()
            except ValueError:
                release_date = None
        
        filme_obj, _ = FilmeAvaliado.objects.get_or_create(title=dados.get("original_title"), year=release_date, imdbID=str(dados.get("id")), img_url=f'https://image.tmdb.org/t/p/w500/{dados.get("poster_path")}',)
        
        Avaliacao.objects.get_or_create(filme=filme_obj, nota=nota, comentario=comentario)
        return redirect(reverse('visualizacao_filme', kwargs={'movieId': movieId}))
    
    
