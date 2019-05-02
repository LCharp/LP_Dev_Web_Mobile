from django.db import models


class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=230)
    sortie = models.CharField(max_length=230)
    AnneeSortie = models.CharField(max_length=4)

def __str__(self):
    return '{self.name}'
