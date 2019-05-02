from td1_1 import *

def test_somme_depenses():
    dep=[("a",2), ("b", 3), ("a",1)]
    assert somme_depenses(dep)==6

def test_somme_depenses_vide():
    assert somme_depenses([]) == 0

def test_depenses_par_personnes():
    dep = [("David",1),("Guillaume",2), ("Kim", 3), ("Aurélien",4)]
    exept = dict(a=3, b=3)

    found  = depenses_par_personne(dep)

    assert len(found) == len(expected)

    for p, d in found:
        assert d == expected(p)
        

