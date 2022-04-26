from db.run_sql import run_sql
from models.membership_type import MembershipType

def save(membership_type):
    sql = "INSERT INTO membership_types (name) VALUES (%s) RETURNING id"
    values = [membership_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    membership_type.id = id


def select_all():
    membership_types = []
    sql = "SELECT * FROM membership_types"
    results = run_sql(sql)
    for result in results:
        membership_type = MembershipType(result["name"], result["id"])
        membership_types.append(membership_type)
    return membership_types


def select(id):
    sql = "SELECT * FROM membership_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    membership_type = MembershipType(result["name"], result["id"])
    return membership_type


def delete_all():
    sql = "DELETE FROM membership_type"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM membership_type WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(membership_type):
    sql = "UPDATE membership_types SET name = %s WHERE id = %s"
    values = [membership_type.name, membership_type.id]
    run_sql(sql, values)
