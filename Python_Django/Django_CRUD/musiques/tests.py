from django.test import TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from musiques.models import Morceau

# Create your tests here.


class MorceauTestCase(TestCase):
    def setUp(self):
        Morceau.objects.create(titre='musique1', artiste='artiste1')
        Morceau.objects.create(titre='musique2', artiste='artiste2')
        Morceau.objects.create(titre='musique3', artiste='artiste3')

    def test_morceau_url_name(self):
        try:
            url = reverse('musiques:morceau-detail', args=[1])
        except NoReverseMatch:
            assert False

    def test_morceau_url(self):
        morceau = Morceau.objects.get(titre='musique1')
        url = reverse('musiques:morceau-detail', args=[morceau.pk])
        response = self.client.get(url)
        assert response.status_code == 200
