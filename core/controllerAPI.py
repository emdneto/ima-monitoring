#!/usr/bin/env python3.7
from flask import Flask
from flask_restful import Resource, Api
import logging
from core.resources import StartMonitoring, ListMonitoring, DeleteMonitoringById #, ListMonitoring, HealthCheck

class ControllerRestfulAPI(object):
    
    app = None
    
    def __init__(self):
        super().__init__()
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self._addResources()
        
    def _addResources(self):
        self.api.add_resource(StartMonitoring, '/necos/ima/start_monitoring')
        self.api.add_resource(ListMonitoring, '/necos/ima/list_monitoring')
        self.api.add_resource(DeleteMonitoringById, '/necos/ima/delete_monitoring')
        
    def run(self):
        self.app.run(host='0.0.0.0', port='5010', debug=True)

    #def main(self):
    #    print('Hello world')

