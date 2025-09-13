import api.urls
from django.shortcuts import redirect
def redirect_home(request):
    return redirect('api/home/')