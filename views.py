from flask import render_template_string, render_template, Flask, request, jsonify
from flask_security import auth_required, current_user, roles_required
from flask_security import SQLAlchemySessionUserDatastore
from flask_security.utils import hash_password

def create_views(app : Flask, user_datastore : SQLAlchemySessionUserDatastore, db ):

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

    @app.route('/register', methods=['POST'])
    def register():

        data = request.get_json()
        

        

        email = data.get('email')
        password = data.get('password')
        role = data.get('role')
 

        if not email or not password or not role:
            return jsonify({'message' : 'invalid input'}), 403

        if user_datastore.find_user(email = email ):
            return jsonify({'message' : 'user already exists'}), 400
        
        if role == 'inst':
            user_datastore.create_user(email = email, password = hash_password(password), active = False, roles = ['inst'])
            db.session.commit()
            return jsonify({'message' : 'Instructor succesfully created, waiting for admin approval'}), 201
        
        elif role == 'stud':
            try :
                user_datastore.create_user(email = email, password = hash_password(password), active = True, roles=['stud']), 201
                db.session.commit()
            except:
                print('error while creating')
            return jsonify({'message' : 'Student successfully created'})
        
        return jsonify({'message' : 'invalid role'}), 400


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