from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.course import Course

import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, course_id, child_first_name, child_last_name, child_age, special_requirements) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.course.id, booking.child_first_name, booking.child_last_name,booking.child_age, booking.special_requirements]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        course = course_repository.select(result["course_id"])
        booking = Booking(member, course, result["child_first_name"], result["child_last_name"], result["child_age"], result["special_requirements"], result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    course = course_repository.select(result["course_id"])
    booking = Booking(member, course, result["child_first_name"], result["child_last_name"], result["child_age"], result["special_requirements"], result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (member_id, course_id, child_first_name, child_last_name, child_age, special_requirements) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [booking.member.id, booking.course.id, booking.child_first_name, booking.child_last_name,booking.child_age, booking.special_requirements]
    run_sql(sql, values)
