from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

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
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    new_booking = Booking(member, course)
    booking_repository.save(new_booking)
    return redirect("/bookings")


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
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    booking = Booking(member, course, id)
    booking_repository.update(booking)
    return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")
