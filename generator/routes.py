# stores roots for the website
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for

routes = Blueprint("routes", __name__)

@routes.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("post request received!")
        selected_adjectives = request.form.getlist("adjective")
        print("Selected Adjectives:", selected_adjectives)
        return redirect("/")
    return render_template("index.html")