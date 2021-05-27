from flask import Blueprint, render_template, url_for, request, redirect, session



main_root_blueprint = Blueprint("main_root", __name__)

@main_root_blueprint.route("/")
def landing_page():
    return render_template("landing_page.html")
