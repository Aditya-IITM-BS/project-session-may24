from flask_security import SQLAlchemySessionUserDatastore
from extensions import db
from flask_security.utils import hash_password
from models import StudyResource


def create_data(user_datastore : SQLAlchemySessionUserDatastore):
    print("creating roles and users") # for debug purposes

    # creating roles

    user_datastore.find_or_create_role(name='admin', description = "Administrator")
    user_datastore.find_or_create_role(name='inst', description = "Instructor")
    user_datastore.find_or_create_role(name='stud', description = "Student")

    # creating initial data

    if not user_datastore.find_user(email = "admin@iitm.ac.in"):
        user_datastore.create_user(email = "admin@iitm.ac.in", password = hash_password("pass"), roles=['admin'])
    if not user_datastore.find_user(email = "inst@iitm.ac.in"):
        user_datastore.create_user(email = "inst@iitm.ac.in", password = hash_password("pass"), roles=['inst'])
    if not user_datastore.find_user(email = "stud@iitm.ac.in"):
        user_datastore.create_user(email = "stud@iitm.ac.in", password = hash_password("pass"), roles=['stud'])

    # create dummy study resource

    db.session.commit()
