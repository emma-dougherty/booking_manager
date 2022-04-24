from flask import Blueprint, Flask, redirect, render_template, request

from models.course import Course
import repositories.course_repository as course_repository


courses_blueprint = Blueprint("courses", __name__)

# INDEX
@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses=courses)


# SHOW
@courses_blueprint.route("/courses/<id>")
def show_course(id):
    booked_members = course_repository.select_members_booked_on_course(id)
    course = course_repository.select(id)
    return render_template("courses/show.html", booked_member=booked_members, course=course)


# NEW
@courses_blueprint.route("/courses/new")
def new_course():
    return render_template("courses/new.html")


# CREATE
@courses_blueprint.route("/courses", methods=["POST"])
def create_course():
    name = request.form["name"]
    date = request.form["date"]
    times = request.form["times"]
    duration = request.form["duration"]
    age_range = request.form["age_range"]
    location = request.form["location"]
    description = request.form["description"]
    new_course = Course(name, date, times, duration, age_range, location, description)
    course_repository.save(new_course)
    return redirect("/courses")


# EDIT
@courses_blueprint.route("/courses/<id>/edit")
def edit_course(id):
    course = course_repository.select(id)
    return render_template('courses/edit.html', course=course)


# UPDATE
@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_course(id):
    name = request.form["name"]
    date = request.form["date"]
    times = request.form["times"]
    duration = request.form["duration"]
    age_range = request.form["age_range"]
    location = request.form["location"]
    description = request.form["description"]
    course = Course(name, date, times, duration, age_range, location, description, id)
    course_repository.update(course)
    return redirect("/courses")


# DELETE
@courses_blueprint.route("/courses/<id>/delete", methods=["POST"])
def delete_course(id):
    course_repository.delete(id)
    return redirect("/courses")
