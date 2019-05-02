from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Film


def film_detail(request,pk):
    return HttpResponse('OK')


class FilmListView(ListView):
    model = Film
    template_name = 'film/test.html'
