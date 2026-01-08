import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.get("/")
def test_mongo():
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(mongo_uri)

    db = client["tpdocker"]
    result = db["checks"].insert_one({"status": "ok"})
    return f"Mongo connected ✅ inserted_id={result.inserted_id}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
