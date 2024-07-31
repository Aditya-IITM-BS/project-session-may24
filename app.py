from flask import Flask
import views
from extentions import db, security, cache
from create_initial_data import create_data
import resources
from flask_caching import Cache
from worker import celery_init_app
import flask_excel as excel
from celery.schedules import crontab
from tasks import daily_reminder, send_email



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

    app.config["CACHE_DEFAULT_TIMEOUT"] = 300
    app.config["DEBUG"] = True
    app.config["CACHE_TYPE"] = "RedisCache"
    app.config["CACHE_REDIS_PORT"] = 6379


    
    cache.init_app(app)
    db.init_app(app)
    excel.init_excel(app)
    

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


    views.create_view(app, user_datastore, cache)

    # connect flask to flask_restful
    resources.api.init_app(app)

    return app

app = create_app()
celery_app = celery_init_app(app)

# daily reminder

@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
    # sender.add_periodic_task(10.0, daily_reminder.s('come again tommorow'), name='add every 10')

    sender.add_periodic_task(
        crontab(hour=17, minute=48, day_of_week=3),
        daily_reminder.s('Happy Mondays!'),
    )


if __name__ == "__main__":
    app.run(debug=True)

