from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from igdb_api_python.igdb import igdb

def home(request,name):
    return render(request, 'jeuxvideo/accueil.html')

def search(request):
    return render(request, 'jeuxvideo/search.html')

def get_key():
    return igdb("b34ee13a58748558d9f273c965c65a7f")

def result_search(request, args):
    igbd = igdb("b34ee13a58748558d9f273c965c65a7f")
    result = igdb.games({
        'search': request.GET['name'],
        'fields': ['name','cover','first_release_date']
    })
    return result.body

from django.views.generic import DetailView
from .models import Jeux

class JeuxListView(ListView):
    model = Jeux
    template_name = 'jeuxvideo/test.html'