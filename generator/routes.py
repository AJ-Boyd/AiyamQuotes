"""
auth: AJ Boyd
date: 6/19/2024
file: routes.py
desc: handles the form requests for the generator
"""

from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, session
from .generate_quote import gen_quote

routes = Blueprint("routes", __name__)

@routes.route('/', methods=['POST', 'GET'])
def home():
    # quote = request.args.get('quote', 'Dummy quote')
    quote = session.get("quote", "")
    return render_template("index.html", quote=quote)

@routes.route('/submit', methods=["POST"])
def submit():
    print("post request received!")
    adjectives = request.form.getlist("adjective")
    print("Selected themes:", adjectives)
    quote = gen_quote(adjectives)
    print(quote)
    session['quote'] = quote
    return redirect(url_for('routes.home', _anchor='middle'))