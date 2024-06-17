from flask import render_template_string
from flask_security import auth_required, current_user, roles_required, roles_accepted


def create_view(app):

    # homepage

    @app.route('/')
    def home():
        return render_template_string(
            """
                <h1> This is homepage </h1>
                <div><a href="/login"> login </a></div>
                <a href="/profile"> Profile page </a>
            """
        )
    
    # profile 
    @app.route('/profile')
    @auth_required('session', 'token')
    def profile():
        return render_template_string(
            """
                <h1> This is profile page </h1>
                <p> Welcome, {{current_user.email}}
                <a href="/logout">logout</a>

            """
        )
    
    @app.route('/inst-dashboard')
    @roles_accepted('inst')
    def inst_dashboard():
        return render_template_string(
            """
                <h1> Instructor profile </h1>
                <p> it should only be visible to instructor</p>
            """
        )

