Polymer : Tiny Amazon
=====================

Librairie Polymer avec bower.

- Initialisation
	- Sous Linux
		- Ouvrir une console de commande.
		- Installer bower avec la commande : ``` npm install -g bower ```
		- Se placer dans le répertoire du projet avec la commande : ``` cd <chemin_jusqu'au_repertoire> ```
        - Si le projet n'a pas été cloné, cloner le avec la commande : ``` git clone https://gitlab.com/LucasCharp/Polymer.git ``` 
            - Puis se placer dans le dossier du projet avec la commande : ``` cd Polymer ```
		- Installer les dépendances du projet avec la commande : ``` bower install ```
        - Lancer l'application avec apache sur google chrome ou chromium

- Détails de l'application
    - index.html : Structure de base de l'application, ce qui sera affiché pour l'utilisateur
	- tiny-app.html : Le décor" de l'application
    - tiny-book-card.html : Traitement et affichage des petites cartes contenant les informations des livres 
    - tiny-book-list.html : Traitement de l'ajout, la suppression et l'édition des livres côté utilisateur
    - tiny-pouchdb.html : Gère les fonctions relatives à la base de données côté serveur 
    
- Autre
    - books.json : Librairie des livres utilisés
    - bower.json : Liste des dépendances et configurations de bower
