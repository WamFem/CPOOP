from flask import Flask, render_template
from app import app

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/purchase")
def purchase_page():
    return render_template("purchase.html")

@app.route("/disclaimer")
def disclaimer_page():
    return render_template("disclamer.html")

