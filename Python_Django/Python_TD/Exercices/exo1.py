def crier(mot="oui"):
    return mot.capitalize() + "!"

print(type(crier))

print(crier())

hurler = crier

print(hurler())

del (crier)

try:
    print(crier())
except NameError as e:
    print(e)

print(hurler())

def creerParler(type="crier"):

    def crier(mot="oui"):
        return mot.capitalize() + "!"

    def cguchoter (mot="oui"):
        return mot.lower() + "...";

    if type == "crier":
        return crier
    else:
        return chuchoter

parler = creerParler()

print(parler)

print (parler())

print (creerParler("chuchoter")())

def faireQuelqueChoseAvant (fonction):
    print ("je fais quelque chose avant d'appeler la fonction")
    print (fonction())

faireQuelqueChoseAvant(crier)