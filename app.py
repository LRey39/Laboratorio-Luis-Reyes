from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Laboratorio de Ciberseguridad"

@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    