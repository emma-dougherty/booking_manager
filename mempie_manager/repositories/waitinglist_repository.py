from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.course import Course

import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

def save(attempted_booking):
    sql = "INSERT INTO waitinglist (member_id, course_id, child_first_name, child_last_name, child_age, special_requirements) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [attempted_booking.member.id, attempted_booking.course.id, attempted_booking.child_first_name, attempted_booking.child_last_name,attempted_booking.child_age, attempted_booking.special_requirements]
    results = run_sql(sql, values)
    id = results[0]['id']
    attempted_booking.id = id
    return attempted_booking


def select_all():
    waitinglist = []
    sql = "SELECT * FROM waitinglist"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        course = course_repository.select(result["course_id"])
        booking = Booking(member, course, result["child_first_name"], result["child_last_name"], result["child_age"], result["special_requirements"], result["id"])
        waitinglist.append(booking)
    return waitinglist


def select(id):
    sql = "SELECT * FROM waitinglist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    course = course_repository.select(result["course_id"])
    booking = Booking(member, course, result["child_first_name"], result["child_last_name"], result["child_age"], result["special_requirements"], result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM waitinglist"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM waitinglist WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE waitinglist SET (member_id, course_id, child_first_name, child_last_name, child_age, special_requirements) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [booking.member.id, booking.course.id, booking.child_first_name, booking.child_last_name,booking.child_age, booking.special_requirements]
    run_sql(sql, values)
