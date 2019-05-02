from django.db import models
from igdb_api_python.igdb import igdb

class Jeux(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    cover = models.CharField(max_length=64)
    first_release_date = models.IntegerField()
        
    def __str__(self):
        return '{self.name}'