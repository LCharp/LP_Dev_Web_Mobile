from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Morceau, Artiste
# Create your views here.


class MorceauDetailView(DetailView):
    model = Morceau
    template_name = 'musiques/morceau.html'


class ArtisteDetailView(DetailView):
    model = Artiste
    template_name = 'musiques/artiste.html'
