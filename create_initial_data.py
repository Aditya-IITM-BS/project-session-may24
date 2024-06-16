from flask_security import SQLAlchemySessionUserDatastore
from extensions import db
from flask_security.utils import hash_password


def create_data(user_datastore : SQLAlchemySessionUserDatastore):
    print("creating roles and users") # for debug purposes

    # creating roles
    if not user_datastore.find_role('admin'):
        user_datastore.create_role(name='admin', description = "Administrator")
    if not user_datastore.find_role('inst'):
        user_datastore.create_role(name='inst', description = "Instructor")
    if not user_datastore.find_role('stud'):
        user_datastore.create_role(name='stud', description = "Student")

    # creating initial data

    if not user_datastore.find_user(email = "admin@iitm.ac.in"):
        user_datastore.create_user(email = "admin@iitm.ac.in", password = hash_password("pass"), roles=['admin'])
    if not user_datastore.find_user(email = "inst@iitm.ac.in"):
        user_datastore.create_user(email = "inst@iitm.ac.in", password = hash_password("pass"), roles=['inst'])
    if not user_datastore.find_user(email = "stud@iitm.ac.in"):
        user_datastore.create_user(email = "stud@iitm.ac.in", password = hash_password("pass"), roles=['stud'])

    db.session.commit()
