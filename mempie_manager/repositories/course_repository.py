from db.run_sql import run_sql
from models.member import Member
from models.course import Course
from models.booking import Booking
import repositories.booking_repository as booking_repository

def save(course):
    sql = "INSERT INTO courses (name, date, times, duration, age_range, capacity, location, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [course.name, course.date, course.times, course.duration, course.age_range, course.capacity, course.location, course.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    course.id = id
    return course


def select_all():
    courses = []
    sql = "SELECT * FROM courses"
    results = run_sql(sql)
    for result in results:
        course = Course(result["name"], result["date"], result["times"], result["duration"], result["age_range"], result["capacity"],result["location"], result["description"],result["id"])
        courses.append(course)
    return courses


def select(id):
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    course = Course(result["name"], result["date"], result["times"], result["duration"], result["age_range"], result["capacity"], result["location"], result["description"],result["id"])
    return course


def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(course):
    sql = "UPDATE courses SET (name, date, times, duration, age_range, capacity, location, description) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [course.name, course.date, course.times, course.duration, course.age_range, course.capacity, course.location, course.description, course.id]
    run_sql(sql, values)


def select_members_booked_on_course(id):
    booked_members = []
    sql = "SELECT * FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.course_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["first_name"], result["last_name"], result["phone_number"], result["email"], result["id"])
        booked_member = Booking(member,result["course_id"],result["child_first_name"],
            result["child_last_name"],result["child_age"],result["special_requirements"])
        booked_members.append(booked_member)
    return booked_members

def number_booked(id):
    booked_members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.course_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["first_name"], result["last_name"], result["phone_number"], result["email"])
        booked_members.append(member)
    return len(booked_members)
