from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
from models.waitinglist import WaitingList
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.waitinglist_repository as waitinglist_repository


home_blueprint = Blueprint("/", __name__)

# INDEX
@home_blueprint.route("/")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("/index.html", bookings=bookings)
