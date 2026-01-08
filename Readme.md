## Exercice 5 — Flask

docker build -t tp-flask .
docker run -d -p 5000:5000 --name flask_tp tp-flask
→ Démarre un serveur web accessible sur http://localhost:5000.

Accès navigateur : http://localhost:5000
Résultat : Hello World from Flask!

## Exercice 6 — Docker Compose + MongoDB

- Création d’une app Flask connectée à MongoDB (pymongo)
- docker compose up -d --build
- Vérification : http://localhost:5000 → insertion OK (inserted_id)

Commandes :
docker compose up -d --build
docker compose ps
docker compose down
