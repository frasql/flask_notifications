from apputils.utils import Utils
from flask import Blueprint, session, render_template, redirect, request, url_for
from models.users.user import User
import models.users.errors as UserErrors


user_blueprint = Blueprint("users", __name__)

@user_blueprint.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            User.register_user(email, password)
            session["email"] = email
            return email
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
                return email
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.html")


@user_blueprint.route('/logout/')
def logout():
    session['email'] = None
    return redirect(url_for('.user_login'))