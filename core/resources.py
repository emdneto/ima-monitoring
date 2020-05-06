from flask_restful import Resource, reqparse
from core.ds import DSManagement
from flask import jsonify
import os
import sys
import uuid



ds = DSManagement()

class StartMonitoring(Resource):
    '''
    Controller /necos/ima/start_monitoring -- Instantiate a new monitoring and store it.
    '''
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('slice_id', type=str, help='Missing Slice Identification', required=True)
        parser.add_argument('slice_name', type=str, help='Missing Slice name', required=True)
        parser.add_argument('bridges', type=list, help='Bridges list', default=[])
        parser.add_argument('ports', type=list, help='ports list', default=[])
        parser.add_argument('edge', type=list, default=[])
        args = parser.parse_args()
        #e2eAdaptorID = uuid.uuid4().hex
        e2eAdaptorID = int(args['slice_id'])
        tryNew = ds._create(e2eAdaptorID, args)
        if not tryNew:
            resp = jsonify('Error')
            resp.status_code = 400
            return resp
        
        args['e2eAdaptor_instance_id'] = e2eAdaptorID
               
        return args
    
class UpdateMonitoring(Resource):
    
    def post(self):
        return 200
    
class ListMonitoring(Resource):
    
    def get(self):
        monitoring_dict= ds._list()
        copy = []
        for key in monitoring_dict.keys():
            copy.append(monitoring_dict[key])
        return copy

class DeleteMonitoringById(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('e2eAdaptor_instance_id', type=int, help='Missing monitoring Identification', required=True)
        args = parser.parse_args()
        e2eAdaptorID = args['e2eAdaptor_instance_id']
        delete = ds._delete(e2eAdaptorID)
        a = type(delete)
        #print(a.__name__)
        
        if a.__name__ == 'tuple':
            dr0 = delete[0]
            dr1 = delete[1]
            b = type(dr1).__name__
            resp = jsonify()
            #resp.type(dr1).__name__ = str(dr1)
            #resp = {type(dr1).__name__: str(dr1)}
            resp.status_code = 400
            return resp
        
        return jsonify(success=True)
        