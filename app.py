from flask import Flask
import views
from extentions import db, security
from create_initial_data import create_data

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "should-not-be-exposed"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
    app.config['SECURITY_PASSWORD_SALT'] = 'salty-password'


    db.init_app(app)

    with app.app_context():

        from models import User, Role
        from flask_security import SQLAlchemyUserDatastore

        user_datastore = SQLAlchemyUserDatastore(db, User, Role) 

        security.init_app(app, user_datastore)

        db.create_all()
        
        create_data(user_datastore)

    app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    app.config['SECURITY_CSRF_PROTECT_MECHANISHMS'] = []
    app.config['SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS'] = True


    views.create_view(app, user_datastore)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)