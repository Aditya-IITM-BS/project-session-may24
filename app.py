from flask import Flask
from extensions import db, security
import views
import create_initial_data
import resources

def create_app():
    app = Flask(__name__)

    # configuration
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'should-not-be-seen'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SECURITY_PASSWORD_SALT'] = 'salty-password'
    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authentication-Token'
    


    # tell flask to use sql_alchemy db
    db.init_app(app)

    with app.app_context():
        from models import User, Role
        from flask_security import SQLAlchemyUserDatastore

        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security.init_app(app, user_datastore)
        
        db.create_all()
        create_initial_data.create_data(user_datastore)

        
    # disable CSRF protection, from WTforms as well as flask security
    app.config["WTF_CSRF_CHECK_DEFAULT"] = False
    app.config['SECURITY_CSRF_PROTECT_MECHANISMS'] = []
    app.config['SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS'] = True

    # setup the view
    views.create_views(app, user_datastore, db)


    # setup api
    resources.api.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()