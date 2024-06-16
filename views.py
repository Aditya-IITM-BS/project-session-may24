from flask import render_template_string
from flask_security import auth_required, current_user, roles_required



def create_views(app):

    # homepage
    @app.route('/')
    def home():
        return render_template_string(
            """
                <h1>Home Page</h1>
            <p><a href="/profile">Go to your profile</a></p>
            <p><a href="/login">Login</a></p>
    
            """
        )

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
    
    @app.route('/inst-dashboard')
    @roles_required('inst')
    def inst_dashboard():
        return render_template_string(
            """
                <h1>this is intructor dashboard</h1>
                <p>This should only be accessable to inst</p>
            """
        )
    
    @app.route('/stud-dashboard')
    @roles_required('stud')
    def stud_dashboard():
        return render_template_string(
            """
                <h1>this is student dashboard</h1>
                <p>This should only be accessable to student</p>
            """
        )