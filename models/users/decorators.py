from functools import wraps
from typing import Callable
from flask import session, flash, redirect, url_for, current_app, request


def login_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("email"):
            flash("Login required!!")
            return redirect(url_for("main_root.landing_page"))
        return func(*args, **kwargs)
    return wrapper


def admin_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("admin") != current_app.config.get("ADMIN", ""):
            flash("Admin required!!")
            return redirect(url_for("users.login"))
        return func(*args, **kwargs)
    return wrapper