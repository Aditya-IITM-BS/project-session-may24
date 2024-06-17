from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from extentions import db


def create_data(user_datastore : SQLAlchemyUserDatastore):

    print('### creating Data #######')


    # create roles
    user_datastore.find_or_create_role(name= 'admin', description = "Administrator")
    user_datastore.find_or_create_role(name= 'inst', description = "Instructor")
    user_datastore.find_or_create_role(name= 'stud', description = "Student")

    # create user data

    if not user_datastore.find_user(email = "admin@iitm.ac.in"):
        user_datastore.create_user(email = "admin@iitm.ac.in", password = hash_password('pass'),active = True, roles=['admin'])
    if not user_datastore.find_user(email = "stud@iitm.ac.in"):
        user_datastore.create_user(email = "stud@iitm.ac.in", password = hash_password('pass'),active = True, roles=['stud'])
    if not user_datastore.find_user(email = "inst@iitm.ac.in"):
        user_datastore.create_user(email = "inst@iitm.ac.in", password = hash_password('pass'),active = True, roles=['inst'])
    if not user_datastore.find_user(email = "random@iitm.ac.in"):
        user_datastore.create_user(email = "random@iitm.ac.in", password = hash_password('pass'),active = True, roles=['inst'])

    db.session.commit()