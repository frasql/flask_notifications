from models.activity import Activity
from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from models.project import Project
from apputils.utils import Utils
from models.users.decorators import login_required
import datetime


activity_blueprint = Blueprint("activities", __name__)


@activity_blueprint.route("/<string:project_id>/")
@login_required
def index(project_id):
    project = Project.find_one_by("_id", project_id)
    ttc = project.total_time
    trm = project.remaining_time
    return render_template("activities/index.html", activities=project.activities, ttc=ttc, trm=trm)


@activity_blueprint.route("/new/<string:project_id>/", methods=["GET", "POST"])
@login_required
def new_activity(project_id):
    if request.method == 'POST':
        activity_name = request.form.get("activity_name")
        description = request.form.get("description")
        order = request.form.get("order")
        time_to_complete = float(request.form.get("time_to_complete"))
        
        project = Project.get_by_id(project_id)
        
        if project.remaining_time < time_to_complete:
            flash(f"Attenzione, aggiungendo questa attività non rispetterai la deadline. I giorni rimasti sono: {project.remaining_time}", "info")
            return redirect(url_for(".new_activity", project_id=project_id))
        
        activity = Activity(activity_name, description, order, time_to_complete, project_id)
        
        activity.save_to_mongo()
        
        flash(f"Activity with title: {activity} created successfully", "info")
        return redirect(url_for(".index", project_id=project_id))
    
    return render_template("activities/new_activity.html", project_id=project_id)


@activity_blueprint.route("/edit/<string:alert_id>/", methods=["GET", "POST"])
@login_required
def edit_activity(alert_id):
    alert = Alert.get_by_id(alert_id)
    note = Note.get_by_id(alert.note_id)
    
    if request.method == "POST":
        end_time = request.form.get("end_time")
        str_end_time = Utils.string_to_datetime(end_time)
        # change alert price
        note.end_time = str_end_time
        note.save_to_mongo()
        return redirect(url_for(".index"))
    return render_template("alerts/edit_alert.html", alert=alert)

 
@activity_blueprint.route("/delete/<string:alert_id>")
@login_required
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session["email"]:
        alert.remove_from_mogno()
    return redirect(url_for(".index"))