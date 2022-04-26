from flask import Blueprint, Flask, redirect, render_template, request

from models.membership_type import MembershipType
from models.member import Member
import repositories.member_repository as member_repository
import repositories.membership_type_repository as membership_type_repository

membership_types_blueprint = Blueprint("memberships", __name__)


# INDEX
@membership_types_blueprint.route("/memberships")
def membership_types():
    membership_types = membership_type_repository.select_all()
    return render_template("memberships/index.html", membership_types=membership_types)


# NEW
@membership_types_blueprint.route("/memberships/new")
def new_membership_type():
    return render_template("memberships/new.html")


# CREATE
@membership_types_blueprint.route("/memberships", methods=["POST"])
def create_membership_type():
    name = request.form["name"]
    benefits = request.form["benefits"]
    new_membership_type = MembershipType(name, benefits)
    membership_type_repository.save(new_membership_type)
    return redirect("/memberships")


# EDIT
@membership_types_blueprint.route("/memberships/<id>/edit")
def edit_membership_type(id):
    membership_type = membership_type_repository.select(id)
    return render_template('memberships/edit.html', membership_type=membership_type)


# UPDATE
@membership_types_blueprint.route("/memberships/<id>", methods=["POST"])
def update_membership_type(id):
    name = request.form["name"]
    benefits = request.form["benefits"]
    membership_type = MembershipType(name, benefits, id)
    membership_type_repository.update(membership_type)
    return redirect("/memberships")


# DELETE
@membership_types_blueprint.route("/memberships/<id>/delete", methods=["POST"])
def delete_membership_type(id):
    membership_type_repository.delete(id)
    return redirect("/memberships")

# # SHOW
# @membership_types_blueprint.route("/memberships/<id>")
# def show_membership_type(id):
#     membership_type = membership_type_repository.select(id)
#     member = member_repository.select_members_with_selected_membership(id)
#     return render_template("memberships/show.html", membership_type=membership_type, member=member)

# SHOW
@membership_types_blueprint.route("/memberships/<id>")
def show_membership_type(id):
    members = member_repository.select_members_with_selected_membership(id)
    membership_type = membership_type_repository.select(id)
    all_members = member_repository.select_all()
    members_with_selected_membership = []
    for member in all_members:
        if member.membership_type.id == int(id):
            members_with_selected_membership.append(member)
    return render_template("memberships/show.html", membership_type=membership_type, members=members, members_with_selected_membership = members_with_selected_membership)

