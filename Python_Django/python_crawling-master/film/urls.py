from django.conf.urls import url, include
from . import views
from .views import FilmListView

app_name = 'film'
urlpatterns = [
    url(r'^listefilm/', FilmListView.as_view(), name='film-liste'),
    ]
