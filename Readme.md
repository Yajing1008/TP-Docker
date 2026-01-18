## Exercice - Manipulation de base des conteneurs
Étapes :
1. Vérifiez la version de Docker :
 docker --version
 → Affiche la version installée de Docker.
2. Listez les images disponibles sur votre machine :
 docker images
 → Montre toutes les images stockées localement.
 3. Téléchargez une image depuis Docker Hub :
 docker pull hello-world
 → Télécharge l'image officielle "hello-world".
4. Exécutez un conteneur à partir de l'image :
 docker run hello-world
 → Lance un conteneur qui affiche un message de bienvenue.
5. Listez les conteneurs en cours d'exécution :
 docker ps
 → Montre les conteneurs actifs.
6. Listez tous les conteneurs (actifs et stoppés) :
 docker ps -a
 → Affiche tout l’historique des conteneurs.
7. Supprimez un conteneur :
 docker rm <ID_conteneur>
8. Supprimez une image :
 docker rmi <ID_image>

## Exercice - Création d'un serveur web avec Docker
Étapes :
1. Vérifiez la version de Docker :
 docker --version
 → Affiche la version installée de Docker.
2. Listez les images disponibles sur votre machine :
 docker images
 → Montre toutes les images stockées localement.
3. Téléchargez une image depuis Docker Hub :
 docker pull hello-world
 → Télécharge l'image officielle "hello-world".
4. Exécutez un conteneur à partir de l'image :
 docker run hello-world
 → Lance un conteneur qui affiche un message de bienvenue.
5. Listez les conteneurs en cours d'exécution :
 docker ps
 → Montre les conteneurs actifs.
6. Listez tous les conteneurs (actifs et stoppés) :
 docker ps -a
 → Affiche tout l’historique des conteneurs.
7. Supprimez un conteneur :
 docker rm <ID_conteneur>
8. Supprimez une image :
 docker rmi <ID_image>

## Exercice - Flask
Objectif : Créer et lancer une application web simple avec Flask à l’aide de Docker.

- Création d’une app Flask (app.py, dockerfile et requirement.txt)
- docker build -t tp-flask .
- docker run -d -p 5000:5000 --name flask_tp tp-flask
→ Démarre un serveur web accessible sur http://localhost:5000.

## Exercice - Docker Compose + MongoDB
Objectif : Déployer une application complexe avec Docker.

- Création d’une app Flask connectée à MongoDB (pymongo) 
- docker compose up -d --build
- Vérification : docker compose ps
- Fermeture et nettoyage:docker compose down

→ Démarre un serveur web accessible sur http://localhost:5000 

→ insertion OK (inserted_id)






