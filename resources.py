from flask_restful import Resource, Api, fields, reqparse, marshal_with
from flask_security import auth_required
from extentions import db
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
    @marshal_with(study_materials_fields)
    def get(self):
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
    @marshal_with(study_materials_fields)
    def get(self):
        all_resources = StudyResource.query.all()
        filtered = [ res for res in all_resources if not res.is_approved ]
        return filtered


api.add_resource(UnapprovedStudyMaterials, '/resources/unapproved')
api.add_resource(StudyMaterials, '/resources')