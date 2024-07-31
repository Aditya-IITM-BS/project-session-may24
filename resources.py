import time
from flask_restful import Resource, Api, fields, reqparse, marshal_with
from flask_security import auth_required, roles_required
from extentions import db, cache
from models import StudyResource

api = Api(prefix='/api')

parser = reqparse.RequestParser() # convert data to dict


parser.add_argument('topic', type=str)
parser.add_argument('content', type=str)
parser.add_argument('creator_id', type=str)

study_materials_fields  = {
    'id' : fields.Integer,
    'topic' : fields.String,
    'content' : fields.String,
    'creator_id': fields.Integer
}

class StudyMaterials(Resource):
    @auth_required('token')
    @cache.cached(timeout=20)
    @marshal_with(study_materials_fields)
    def get(self):
        time.sleep(3) # artificial slow processing
        all_resources = StudyResource.query.all()
        filtered = [ res for res in all_resources if res.is_approved]
        return filtered
    
    
    @auth_required('token')
    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(topic = args.topic, content= args.content, creator_id = args.creator_id)
        db.session.add(study_resource)
        db.session.commit()
        return {'message' : 'resource created'}, 200

class UnapprovedStudyMaterials(Resource):
    @auth_required('token')
    @roles_required('inst')
    @cache.cached(timeout=5)
    @marshal_with(study_materials_fields)
    def get(self):
        unapproved_resources = StudyResource.query.filter_by(is_approved=False).all()
        return unapproved_resources

api.add_resource(StudyMaterials, '/resources')
api.add_resource(UnapprovedStudyMaterials, '/resources/unapproved')