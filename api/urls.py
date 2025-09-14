from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('buscarfilmes/', views.buscar_filmes_view, name='buscar_filmes' ),
    path('visualizacao_filme/<int:movieId>/', views.visualizar_filme, name='visualizacao_filme'),
    path('criar_avaliacao/<int:movieId>', views.criar_avaliacao, name='criar_avaliacao'),
]