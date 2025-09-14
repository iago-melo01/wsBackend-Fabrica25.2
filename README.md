# 🎬 Catálogo de Filmes com Avaliações

Este projeto é uma aplicação web feita em **Django** que consome a [API do TMDb (The Movie Database)](https://www.themoviedb.org/documentation/api) para buscar informações de filmes e permite que usuários adicionem avaliações e comentários locais.

---

## 🚀 Funcionalidades

- 🔍 **Busca de filmes** pelo título (usando endpoint `/search/movie` da TMDb).
- 📖 **Detalhes do filme**: exibe título, data de lançamento, sinopse, gêneros, idioma original, orçamento/receita, produtoras etc.
- 🖼️ **Exibição do pôster** oficial (quando disponível).
- ⭐ **Avaliações locais**: formulário para que o usuário dê uma nota (1–10) e escreva um comentário.
- 💬 **Listagem de comentários** salvos no banco de dados, vinculados ao filme.
- 🌎 Interface em **português (pt-BR)**.

---

## 🛠️ Tecnologias

- [Django](https://www.djangoproject.com/) — backend e templates.
- [Requests](https://docs.python-requests.org/) — consumo da API TMDb.
- [dotenv](https://pypi.org/project/python-dotenv/) — gerenciamento de variáveis de ambiente.
- **HTML + CSS** — templates estilizados.
- **Banco de dados** (pode ser SQLite para desenvolvimento, ou Postgres/MySQL em produção).

---

## 📂 Estrutura simplificada


## ⚙️ Instalação e execução

1. Clone o repositório:
   ```bash //Execute isso no git bash ou no bash da sua IDE
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo


2. Crie e ative o ambiente virtual:
//execute esses comandos no terminal da sua IDE
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Instale as dependências:

pip install -r requirements.txt

4.Configure o arquivo .env na raiz do projeto:
TMDB_API_KEY=sua_chave_aqui

// Faça isso alterando o valor (sua_chave_aqui) para o respectivo valor da sua api key gerada no site abaixo
https://developer.themoviedb.org/reference/intro/getting-started


5.Execute as migrações:
//dê esses comandos separadamente no terminal da sua IDE
python manage.py makemigrations
python manage.py migrate

6.Inicie o servidor:

python manage.py runserver

7.Acesse em http://127.0.0.1:8000/

📚 Endpoints principais

/ → Home (formulário de busca)

/buscar/?q=batman → Resultados da pesquisa

/visualizacao_filme/<movieId> → Detalhes do filme + avaliações

/visualizacao_filme/<movieId>/avaliar → POST de avaliação

🗃️ Modelos principais
FilmeAvaliado

title — título original

year — data de lançamento

imdbID — ID do filme na TMDb (⚠️ nome pode ser trocado para tmdb_id)

img_url — pôster

Avaliacao

filme — relação com FilmeAvaliado

nota — inteiro (1–10)

comentario — texto do usuário
