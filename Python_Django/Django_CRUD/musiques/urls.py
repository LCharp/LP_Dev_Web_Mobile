from django.conf.urls import url, include
from . import views
from .views import MorceauDetailView, ArtisteDetailView

app_name = 'musiques'
urlpatterns = [
    url(r'^(?P<pk>\d+)/detail$', MorceauDetailView.as_view(), name='morceau-detail'),
    url(r'^(?P<pk>\d+)/detailArtiste$',
        ArtisteDetailView.as_view(), name='artiste-detail'),
]
