from flask import jsonify, render_template, render_template_string, request, send_file
from flask_security import auth_required, current_user, roles_required, roles_accepted, SQLAlchemyUserDatastore
from flask_security.utils import hash_password, verify_password
from extentions import db
from models import StudyResource
from datetime import datetime
from tasks import create_csv
from flask_excel import make_response_from_query_sets
from celery.result import AsyncResult


def create_view(app, user_datastore : SQLAlchemyUserDatastore, cache):

    # cache test
    @app.route('/cache-test')
    @cache.cached(timeout = 5)
    def cache_test():
        return jsonify({"time" : datetime.now()})

    # homepage

    @app.route('/')
    def home():
        return render_template('index.html')
    

    @app.route('/user-login', methods=['POST'])
    def user_login():

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        
        if not email or not password:
            return jsonify({'message' : 'not valid email or password'}), 404
        
        user = user_datastore.find_user(email = email)

        if not user:
            return jsonify({'message' : 'invalid user'}), 404
        
        if verify_password(password, user.password):
            return jsonify({'token' : user.get_auth_token(), 'role' : user.roles[0].name, 'id' : user.id, 'email' : user.email }), 200
        else:
            return jsonify({'message' : 'wrong password'})

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
    @auth_required('token')
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
    
    # @auth_required('token')
    @roles_required('admin')
    @app.route('/activate-inst/<id>' )
    def activate_inst(id):

        user = user_datastore.find_user(id=id)
        if not user:
            return jsonify({'message' : 'user not present'}), 404

        # check if inst already activated
        if (user.active == True):
            return jsonify({'message' : 'user already active'}), 400

        user.active = True
        db.session.commit()
        return jsonify({'message' : 'user is activated'}), 200
    
    # activate study resource
    @app.route('/verify-resource/<id>')
    @roles_required('inst')
    def activate_resource(id):
        resource = StudyResource.query.get(id)
        if not resource:
            return jsonify({'message' : 'invalid id'}), 400
        resource.is_approved = True
        db.session.commit()
        return jsonify({'message' : 'resource is now approved'}), 200

    # endpoint to get inactive inst
    @roles_required('admin')
    @app.route('/inactive_instructors', methods=['GET'])
    def get_inactive_instructors():
        # Query for all users
        all_users = user_datastore.user_model().query.all()
        
        # Filter users to get only inactive instructors
        inactive_instructors = [
            user for user in all_users 
            if not user.active and any(role.name == 'inst' for role in user.roles)
        ]
        
        # Prepare the response data
        results = [
            {
                'id': user.id,
                'email': user.email,
            }
            for user in inactive_instructors
        ]
        
        return jsonify(results), 200

    @app.route('/celery-task')
    def celery_task_view():
        task = celery_task.delay() # function to execute this celery task
        return jsonify({'taskid' : task.id}), 200

    @app.route('/download-csv')
    def download_csv():
        task = create_csv.delay()

        return jsonify({'task-id' : task.id}), 200
    
    @app.get('/get-csv/<id>')
    def get_csv(id):
        res = AsyncResult(id)

        if res.ready():
            return 'task ready'
        else:
            return 'task pending', 425 