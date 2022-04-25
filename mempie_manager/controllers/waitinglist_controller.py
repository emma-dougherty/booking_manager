from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
from models.waitinglist import WaitingList
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.waitinglist_repository as waitinglist_repository


waitinglists_blueprint = Blueprint("waitinglists", __name__)

# INDEX
@waitinglists_blueprint.route("/waitinglists")
def waitinglists():
    waitinglists = waitinglist_repository.select_all()
    return render_template("waitinglists/index.html", waitinglists=waitinglists)


# NEW
@waitinglists_blueprint.route("/waitinglists/new")
def new_waiting():
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template("waitinglists/new.html", members=members, courses=courses)


# CREATE
@waitinglists_blueprint.route("/waitinglists", methods=["POST"])
def create_waitinglist():
    member_id = request.form["member_id"]
    course_id = request.form["course_id"]
    child_first_name = request.form["child_first_name"]
    child_last_name = request.form["child_last_name"]
    child_age = request.form["child_age"]
    special_requirements= request.form["special_requirements"]
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    num_on_course = course.number_booked()
    if num_on_course > course.capacity:
        new_booking = Booking(member, course, child_first_name, child_last_name, child_age, special_requirements)
        booking_repository.save(new_booking)
        return redirect("/bookings")


# EDIT
@waitinglists_blueprint.route("/waitinglists/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template('waitinglists/edit.html', booking=booking, members=members, courses=courses)


# UPDATE
@waitinglists_blueprint.route("/waitinglists/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    course_id = request.form["course_id"]
    child_first_name = request.form["child_first_name"]
    child_last_name = request.form["child_last_name"]
    child_age = request.form["child_age"]
    special_requirements= request.form["special_requirements"]
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    booking = Booking(member, course, child_first_name, child_last_name, child_age, special_requirements)
    booking_repository.update(booking)
    return redirect("/waitinglists")


# DELETE
@waitinglists_blueprint.route("/waitinglists/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/waitinglists")
