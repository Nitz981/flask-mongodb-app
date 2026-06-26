from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.flask_db
collection = db.data

# Home Route
@app.route("/")
def home():
    now = datetime.now()
    return jsonify({
        "message": "FarAlpha Kubernetes Assignment Running Successfully",
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%H:%M:%S")
    })

# Insert and Fetch Data
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({
            "status": "Data inserted successfully"
        }), 201

    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200

# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)