import collections

Carte = collections.namedtuple('Carte', ['rang','couleur'])

class JeuCartes:
    rangs = [str(n) for n in range(2,11)] + list('VDRA')
    couleurs = ['pique', 'coeur', 'carreau', 'trèfle']

    def __init__(self):
        self._cartes = [Carte(rang, couleur)
                         for couleur in self.couleur 
                         for rang in self.rangs]

    def __len__(self):
        return len(self.cartes)     

    # l(0)

    def __getitem__(self, i):
        return self.cartes[i]

    # del l(0)

    def __delitem__(self, i):
       # self.cartes.remove(i)
        del self.carte[i]

    # for i in l

    def __iter__(self):
        
        return iter(self.cartes)

        #Avec yield pas besoin de return
        #for c in self.cartes:
        #    yield c

    def tri_bridge(carte):
        coul_val = dict(trefle=0, carreau=1, coeur=2, pique=3)
        try:
            return (int[carte.rang], coul_val[carte.couleur])
        except:
            cout_rang ={
                'V': 11,
                'D':12,
                'R':13,
                'A':14
            }
            return (cout_rang[carte,rang], coul_val[carte,couleur])

    ValetPique = Carte('Carte', ['V','pique'])
    print ValetPique
    jc=JeuCartes()

coul_val = dict (trèfle=0, carreau=1, coeur=2, pique=3)
        
def tri_decroissant(x):
    return -x


    class vecteur:
        def __init__(self, x, y):
            self.x, self.y=x,y

        def __str__(self):
            return '({} ; {})'.format(self.x, self.y)

        def __repr__(self):
            return 'vecteur :' + str(self)

        def __add__(self, other):
            pass
        
        def __mul__(self, other):
            return vecteur(self.x * other.x, self.y * other.y)
        