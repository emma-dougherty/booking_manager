from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
from models.waitinglist import WaitingList
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.waitinglist_repository as waitinglist_repository


bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)


# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template("bookings/new.html", members=members, courses=courses)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    course_id = request.form["course_id"]
    child_first_name = request.form["child_first_name"]
    child_last_name = request.form["child_last_name"]
    child_age = request.form["child_age"]
    special_requirements= request.form["special_requirements"]
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    num_on_course = course_repository.number_booked(course_id)
    if num_on_course < course.capacity:
        new_booking = Booking(member, course, child_first_name, child_last_name, child_age, special_requirements)
        booking_repository.save(new_booking)
        return redirect("/bookings")
    if num_on_course >= course.capacity:
        new_waitinglist = WaitingList(member, course, child_first_name, child_last_name, child_age, special_requirements)
        waitinglist_repository.save(new_waitinglist)
        attempted_booking_list = waitinglist_repository.select_all()
        return render_template("/waitinglists/index.html", waitinglists=attempted_booking_list)


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, courses=courses)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    course_id = request.form["course_id"]
    child_first_name = request.form["child_first_name"]
    child_last_name = request.form["child_last_name"]
    child_age = request.form["child_age"]
    special_requirements= request.form["special_requirements"]
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    booking = Booking(member, course, child_first_name, child_last_name, child_age, special_requirements, id)
    booking_repository.update(booking)
    return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")
