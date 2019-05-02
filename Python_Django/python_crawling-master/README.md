Internet Game Database
======================

Application Django de listing de jeux vidéo, utilisant l'API d'IGDB.com ( https://www.igdb.com/ ) et le scrapping de données de wikipédia ( https://en.wikipedia.org/wiki/List_of_films_based_on_video_games )

- Initialisation
	- Sous Linux
		- Ouvrir une console de commande.
		- Créer un "virtualenv" avec la commande : ``` virtualenv -p python3 ~/venv3 ```
		- Initialiser l'environnement avec la commande : ``` source ~/venv3/bin/activate ```
		- Installer Django avec la commande : ``` pip install django ```
		- Se placer dans le repertoire du projet avec ``` cd <chemin_jusqu'au_repertoire> ```
		- Lancer le serveur web de django avec la commande : ``` ./manage.py runserver ```
	
	- Sous Windows
		- Télécharger la dernière version de Python (au mieux) : https://www.python.org/downloads/
		- Télécharger et extraire la dernière version de Django (au mieux) : https://www.djangoproject.com/download/
		- Aller dans : Panneau de configuration -> Tous les Panneaux de configuration -> Système -> Paramètres système avancés -> Variables d'environnement
		- Puis ajouter à la variable "Path" : ``` ;<Chemin_dossier_Python>;<Chemin_dossier_Python>\Lib\site-packages\django\bin ```
		- Retourner dans le dossier de Django, puis, dans une console de commande, taper : ``` python setup.py install ```
		- Ensuite, lancer le serveur web de django avec la commande : ``` python manage.py runserver ```
	
- Lancement
	- Lancer le serveur comme dit précédemment
	- Ouvrir le navigateur de votre choix, puis mettre en URL : http://localhost:8000/jeuxvideo/home
	

- Détails de l'application
    - migrations: Sous-application aidant à initialiser les changements de models.py dans la base de données
    - static: Contient les templates statiques (javascript, css)
    - admin.py
    - models.py: Contient chaque table sous forme de modèle Python. Django les utilise pour former la base de données.
    - urls.py: Les différentes URL initialisées, pour que Django puisse s'en servir pour router l'application.
    - utils.py: Contient les fonctions de l'application.
    - views.py: Code principal du projet, permet de filtrer, modifier et initialiser les vues html.
	
- Autre
	- manage.py: Script Django requis pour lancer le serveur, faire les migrations à la base de données, et ainsi à la synchroniser.