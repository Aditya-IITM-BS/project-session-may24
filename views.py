from flask import render_template_string, render_template, Flask, request
from flask_security import auth_required, current_user, roles_required
from flask_security import SQLAlchemySessionUserDatastore

def create_views(app : Flask, user_datastore : SQLAlchemySessionUserDatastore ):

    # homepage
    @app.route('/')
    def home():
        return render_template('index.html') # entry point to vue frontend

    # profile
    @app.route('/profile')
    @auth_required('token', 'session')
    def profile():
        return render_template_string(
            """
                <h1> this is homepage </h1>
                <p> Welcome, {{current_user.email}}</p>
                <p> Role :  {{current_user.roles[0].description}}</p>
                <p><a href="/logout">Logout</a></p>
            """
        )

    @app.route('/register')
    def register():
        data = request.form
        if data.role == 'Instructor':
            user_datastore.find_user(**data, active = False, roles = ['inst'])
        elif data.role == 'Student':
            user_datastore.create_user(**data, active = True, roles=['stud'])


    @app.route('/inst-dashboard')
    @roles_required('inst')
    def inst_dashboard():
        return render_template_string(
            """
                <h1>this is instructor dashboard</h1>
                <p>This should only be accessible to inst</p>
            """
        )
    
    @app.route('/stud-dashboard')
    @roles_required('stud')
    def stud_dashboard():
        return render_template_string(
            """
                <h1>this is student dashboard</h1>
                <p>This should only be accessible to student</p>
            """
        )