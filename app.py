from flask import Flask
import views
from extentions import db, security, cache
from create_initial_data import create_data
import resources
from worker import celery_init_app

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "should-not-be-exposed"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
    app.config['SECURITY_PASSWORD_SALT'] = 'salty-password'

    # configure token
    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authentication-Token'
    app.config['SECURITY_TOKEN_MAX_AGE'] = 3600 #1hr
    app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = True

    # cache config
    app.config["DEBUG"]= True         # some Flask specific configs
    app.config["CACHE_TYPE"]= "RedisCache"  # Flask-Caching related configs
    app.config['CACHE_REDIS_HOST'] = 'localhost'
    app.config['CACHE_REDIS_PORT'] = 6379
    app.config['CACHE_REDIS_DB'] = 0
    app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
    app.config["CACHE_DEFAULT_TIMEOUT"]= 300
    # app.config["CACHE_REDIS_PORT"] = 6379

    cache.init_app(app)
    db.init_app(app)

    with app.app_context():

        from models import User, Role
        from flask_security import SQLAlchemyUserDatastore

        user_datastore = SQLAlchemyUserDatastore(db, User, Role) 

        security.init_app(app, user_datastore, register_blueprint=False)

        db.create_all()
        
        create_data(user_datastore)

    # disable CSRF security
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    app.config['SECURITY_CSRF_PROTECT_MECHANISHMS'] = []
    app.config['SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS'] = True


    views.create_view(app, user_datastore, cache)

    # connect flask to flask_restful
    resources.api.init_app(app)


    return app

celery_app = None

if __name__ == "__main__":
    app = create_app()

    # cerating celery application
    celery_app = celery_init_app(app)
    app.run(debug=True)