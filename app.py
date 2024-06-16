from flask import Flask
from extensions import db, security
import views
import create_initial_data

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

    # setup the view
    views.create_views(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()