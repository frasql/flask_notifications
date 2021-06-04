from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from models.project import Project
from models.activity import Activity
from apputils.utils import Utils
from models.users.decorators import login_required
import datetime


project_blueprint = Blueprint("projects", __name__)


@project_blueprint.route("/")
@login_required
def index():
    projects = Project.find_many_by("user_email", session["email"])
    return render_template("projects/index.html", projects=projects)


@project_blueprint.route("/new/", methods=["GET", "POST"])
@login_required
def new_project():
    if request.method == 'POST':
        project_name = request.form.get("project_name")
        description = request.form.get("description")
        deadline = request.form.get("deadline")
        try:
            
            deadline = float(deadline)
        except TypeError as e:
            raise TypeError(f"Unable to convert end time to datetime object {e}")

        project = Project(project_name, description, deadline, session["email"])
        
        project.save_to_mongo()
        
        flash(f"Project with title: {project_name} created successfully", "info")
        return redirect(url_for(".index"))
    
    return render_template("projects/new_project.html")


@project_blueprint.route("/edit/<string:alert_id>/", methods=["GET", "POST"])
@login_required
def edit_alert(alert_id):
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

 
@project_blueprint.route("/delete/<string:alert_id>")
@login_required
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session["email"]:
        alert.remove_from_mogno()
    return redirect(url_for(".index"))