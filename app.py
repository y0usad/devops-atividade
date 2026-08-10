# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá! Esta é uma aplicação Dockerizada para a atividade de DevOps."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)