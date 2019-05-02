from django.db import models

# Create your models here.


class Artiste(models.Model):
    nom = models.CharField(max_length=64)


class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste_fk = models.ForeignKey(
        Artiste, on_delete=models.CASCADE, null=True)
    date_sortie = models.DateField(null=True)

    def __str__(self):
        return '{self.titre} ({self.artiste})'.format(self=self)
