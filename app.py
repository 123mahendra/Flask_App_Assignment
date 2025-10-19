from flask import Flask,jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return "Welcome to my REST API!"

@app.get("/api/v1/cat")
def get_cat():
    cat = [{
        "cat_id": "2",
        "name": "Lucky",
        "birthdate": "2025-10-10",
        "weight": 5,
        "owner": "Mahendra",
        "image": "https://www.pexels.com/photo/orange-tabby-kitten-2181171/"
    }]
    return jsonify(cat)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)