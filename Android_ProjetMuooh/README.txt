L'application est développer avec android studio.

Version android choisie: android 26

Librairie utilisé: Zxing (https://github.com/zxing/zxing)

Application: Application de génération de qrcode automatique et dynamique.

Information Muooh:
Les qrcode sont générer à l'aide de la librairie Zxing.
L'application a été développé pour un environement local sans server php.
Avec l'ajout d'un server php, certaine conditon doivent être ajouter au traitement sur la base de donnée sqlite.
Il faudra en effet gérer l'id inséré dans la base de donné local pour qu'il corresponde à un id "client" intégrer
manuellement par l'entreprise Muooh sur la base de donnée du server php. Ceci afin d'empecher un client de crée des identifiant et donc de surcharger la
base de donnée du server. De plus cela permet à Muooh de gérer au mieux ses clients en leur attribuant un id
unique.
Cette identifiant unique liée a chaque client et gérer coté server par Muooh permettra entre autre (comme c'est deja le cas en local)
pour les clients de modifier leur informations personnel (nom d'entreprise, adresse etc...).
Dans notre application, le choix a été fait d'ooculter la gestion avec un server distant pour ne pas surcharger le code pouvant être par la suite intégrer à une application Muooh dédié au 
revendeur.
En effet, toute la gestion des donnée en interne par l'entreprise n'étant pas connu j'ai chosisi de développer une application aussi générique que possible pour facilité une futur intégration
sachant que plusieurs point sont a prendre en compte.
L'entreprise Muooh fournissant l'application à ses clients (entreprise liée au groupe), la liaison entre la base de donnée de chaque application (bd local) et celle distante (bd du server) 
se fera en interne, par l'entreprise (n'ayant pas accés au server ceci n'est pas possible dans la phase de développement du projet).
Cette dernière devra initialiser l'application sur un Device et devra derterminer à quel entreprise l'appareil est liée (quel id sera incorporé nativement à la bd local l'application). 
Puis, à l'aide de l'ecran de démarage pourra facilement insérer les information d'un entreprise (nom et adresse d'une entreprise).
Ce fesant, l'application sera initialisé avec un id unique connu par la base de donnée du serveur et celle de la bd local et un premier jeu de données propre à l'entreprise sera initialisé à la fois 
sur le serveur php et sur la base de donnée local.
Cette section du développement pourra et devra être développer en interne par l'entreprise Muooh afin de correctement liée l'application fournie avec leurs serveur.

Cocernant mon application local, un premier écran est afficher au lancement de l'application. Ce dernier permet de crée la base de donnée local et les informations d'un revendeur (nom et adresse 
du revendeur).
Une fois ces informations renseigner, l'application nous envoi sur la page principal de l'application.
Cette derniere est découper en 3 partie. La Première reprend le nom et l'adresse du revendeur. La 2ème est le qrcode liée à l'application et la 3ème simule un scan du qrcode à l'aide d'un bouton.
Le développement est penser pour qu'en cas de clique (scan du qrcode), celui ci change tout en gardant les informations du qrcode (nom et adresse).
Dans ce but, une chaine aléatoire est générer et ajouter au dessin du qrcode (elle est ajouter en bd local est devra être tester à chaque scan du coté du server afin de vérifier que le qrcode scanner 
est bien le qrcode actuel). (cette chaine devra aussi être modifier en bd server à chaque fois qu'elle est modifier localement afin de garantir une intégriter des données)
Ceci permettra entre autre de limiter la duplication de qrcode. En effet un client pour dupliquer le qrcode devra connaitre cette chaine aléatoire qui est changer à chaque scan.
Par ailleurs, un écran de paramètre est ajouter à l'application afin qu'un revendeur puisse modifer ses informations. Le formulaire est pour le moment basique mais peux intégrer d'autre informations
tel que les contact du revendeur mais devra être gérer du coté de la base de donnée local et server pour sauvegarder ces données.

Ainsi, l'application permet en local de générer des qrcode dynamiquement (chaque qrcode étant different des précédent). Elle permet entre autre à un revendeur de modifier ses informations personnel.
Enfin elle permet entre autre à une personne initialisant l'application de renseigner les informations d'un revendeur.