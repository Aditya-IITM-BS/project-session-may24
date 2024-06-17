from flask_restful import Resource, Api, reqparse, marshal_with, fields
from models import StudyResource, db
from flask_security import auth_required

parser = reqparse.RequestParser() # if a client is sending data, it will convert into a dict
parser.add_argument('topic', type=str, help = "Topic should be string", required = True)
parser.add_argument('content', type=str, help = "Topic should be string")

api = Api(prefix='/api')

# marshal with is used to serialize the data coming from database

study_material_fields = {
    'id' : fields.Integer,
    'topic' : fields.String,
    'content' : fields.String,
    'creator_id' : fields.Integer
}


class StudyMaterial(Resource):

    # get request will run this function (retrieve)
    @auth_required('token','session')
    @marshal_with(study_material_fields)
    def get(self):
        all_study_resources = StudyResource.query.all()
        return all_study_resources
    
    # post request will run this function (create)
    @auth_required('token', 'session')
    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(creator_id = 1, is_approved = False, **args )
        db.session.add(study_resource)
        db.session.commit()
        return {"message" : "resource created"}
    
api.add_resource(StudyMaterial, '/resources')