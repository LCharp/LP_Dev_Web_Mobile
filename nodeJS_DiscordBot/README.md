Eraser bot
==========

Bot Discord en javascript, utilisant l'API discord.js ( https://discord.js.org ).

- Initialisation
	- Sous Linux
		- Ouvrir une console de commande.
		- Installer node js avec la commande : ``` sudo apt install -y nodejs ```
		- Se placer dans le répertoire du projet avec la commande : ``` cd <chemin_jusqu'au_repertoire> ```
        - Si le projet n'a pas été cloné, cloner le avec la commande : ``` git clone https://gitlab.com/LucasCharp/Projet_DiscordBot_nodeJS.git ``` 
            - Puis se placer dans le dossier du projet avec la commande : ``` cd Projet_DiscordBot_nodeJS```
        - Lancer le bot avec la commande : ``` node eraserBot/app.js ```
	
	- Sous Windows
		- Installer node js : https://nodejs.org/en/download/ 
		- Ouvrir une console de commande
        - Se placer dans le répertoire du projet avec la commande : ``` cd <chemin_jusqu'au_repertoire> ```
        - Si le projet n'a pas été cloné, cloner le avec la commande : ``` git clone https://gitlab.com/LucasCharp/Projet_DiscordBot_nodeJS.git ``` 
            - Puis se placer dans le dossier du projet avec la commande : ``` cd Projet_DiscordBot_nodeJS```
        - Lancer le bot avec la commande : ``` node eraserBot/app.js ```
	
- Lancement
	- Lancer le bot comme dit précédemment
	- Se connecter à Discord via un navigateur à l'adresse : https://discordapp.com/channels/@me
        - Ou installer Discord et s'y connecter via le lien de téléchargement : https://discordapp.com/download (identifie automatiquement votre OS)
    - Inviter le bot sur un serveur où vous avez la permission "Gérer le serveur", via le lien : https://discordapp.com/oauth2/authorize?client_id=405684553357721610&scope=bot&permissions=285326390 
	

- Détails de l'application
    - app.js : Structure de base du bot : connexion à l'API et gestion des messages entrant
    - command.js : Récupère les commandes des utilisateurs, et d'utiliser les fonctionnalités correspondantes 
    - chat.js : Lance le bot dans une boucle de discussion ou non
    - addChat.js : Discute avec un utilisateur suivant la discussion donnée
    - google.js : Envoie le résultat d'une recherche google demandée
    - erase.js : Efface des messages indésirables selon le contenu du message, puis averti l'utilisateur de son comportement
	
- Autre
    - chat.json : Librairie de mots utilisée pour la fonction de chat
    - token.json : Contenu du token utilisée pour la connexion à l'API