from flask import Flask
import views
from extentions import db, security
from create_initial_data import create_data
import resources

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "should-not-be-exposed"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
    app.config['SECURITY_PASSWORD_SALT'] = 'salty-password'

    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authentication-Token'
    app.config['SECURITY_TOKEN_MAX_AGE'] = 3600 #1hr 
    app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = True

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

    # connect flask to flask_restful
    resources.api.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)