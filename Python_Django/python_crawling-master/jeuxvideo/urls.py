from django.conf.urls import url, include
from . import views
from .views import JeuxListView, search, result_search

app_name = 'jeuxvideo'
urlpatterns = [
    url(r'^home/(\w+)?', views.home, name='home'),
    url(r'^listejeux/', JeuxListView.as_view(), name='jeux-liste'),
    url(r'^search/', search, name='search'),
    url(r'^result/(\w+)?', result_search, name='result'),
    ]