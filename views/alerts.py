from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from models.alert import Alert
from models.note import Note
from apputils.utils import Utils
from models.users.decorators import login_required
import datetime


alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
@login_required
def index():
    alerts = Alert.find_many_by("user_email", session["email"])
    return render_template("alerts/index.html", alerts=alerts)


@alert_blueprint.route("/new/", methods=["GET", "POST"])
@login_required
def new_alert():
    if request.method == 'POST':
        alert_name = request.form.get("alert_name")
        title = request.form.get("title")
        description = request.form.get("description")
        start_time = datetime.datetime.utcnow()
        end_time = request.form.get("end_time")
        
        try:
            end_time = Utils.string_to_datetime(end_time)
        except TypeError:
            raise TypeError("Unable to convert end time to datetime object")

        note = Note(title, description, start_time, end_time)
        note.save_to_mongo()

        Alert(alert_name, note._id, session["email"]).save_to_mongo()
        
        flash(f"Alert created successfully at {end_time} with title: {title}", "info")
        return redirect(url_for("users.homepage"))
    
    return render_template("alerts/new_alert.html")


@alert_blueprint.route("/edit/<string:alert_id>/", methods=["GET", "POST"])
@login_required
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if request.method == "POST":
        end_time = request.form.get("end_time")
        # change alert price
        alert.note.end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M')

        alert.save_to_mongo()

        return redirect(url_for(".index"))
    return render_template("alerts/edit_alert.html", alert=alert)

 
@alert_blueprint.route("/delete/<string:alert_id>")
@login_required
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session["email"]:
        alert.remove_from_mogno()
    return redirect(url_for(".index"))