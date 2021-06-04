from apputils.utils import Utils
from flask import Blueprint, session, render_template, redirect, request, url_for
from models.users.user import User
from models.alert import Alert
from models.project import Project
import models.users.errors as UserErrors
from models.users.decorators import login_required


user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/homepage/", methods=["GET"])
@login_required
def homepage():
    user_email = session["email"]
    email = user_email.split("@")[0]
    alerts_number = len(Alert.find_many_by("user_email", user_email))
    projects_number = len(Project.find_many_by("user_email", user_email))
    return render_template("users/homepage.html", email=email, alerts_number=alerts_number, projects_number=projects_number)

@user_blueprint.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            User.register_user(email, password)
            session["email"] = email
            return redirect(url_for(".homepage"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.html")


@user_blueprint.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            if User.is_login_valid(email, password):
                session["email"] = email
                return redirect(url_for(".homepage"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.html")


@user_blueprint.route('/logout/')
@login_required
def logout():
    session['email'] = None
    return redirect(url_for('main_root.landing_page'))