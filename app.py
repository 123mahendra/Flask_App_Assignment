from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "Welcome to my REST API!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)