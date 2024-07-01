from flask import jsonify, render_template, render_template_string, request
from flask_security import auth_required, current_user, roles_required, roles_accepted, SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from extentions import db


def create_view(app, user_datastore : SQLAlchemyUserDatastore):

    # homepage

    @app.route('/')
    def home():
        return render_template('index.html')
    

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not email or not password or role not in ['inst', 'stud']:
            return jsonify({"message" : "invalid input"})
        
        if user_datastore.find_user(email=email):
            return jsonify({"message" : "user already exists"})
        
        # inst active = False
        if role == 'inst':
            active = False
        elif role == 'stud':
            active = True
        try:    
            user_datastore.create_user(email = email, password = hash_password(password), roles = [role], active = active )
            db.session.commit()
        except:
            print('error while creating')
            db.session.rollback()
            return jsonify({'message' : 'error while creating user'}), 408
        
        return jsonify({'message' : 'user created'}), 200
        
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
    
    

