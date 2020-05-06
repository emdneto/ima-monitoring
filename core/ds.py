import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
              
class DataStorer(object):
    
    def __init__(self):
        
        self.e2eActiveAdaptors = {}
        self.instances = []

class DSManagement(DataStorer):
    
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("DSManagement")

    @staticmethod
    def _checkParams(e2eAdaptorID, data): 
        
        if e2eAdaptorID != None and data != {}:
            return True
        
        return False
            
    
    def _create(self, uuid=None, data={}):
        e2eAdaptorID = int(uuid)
        
        if not self._checkParams(e2eAdaptorID, data):    
            self.log.debug('Failed to create. None values. Check the given parameters.')
            return False
        
                        
        if e2eAdaptorID in self.e2eActiveAdaptors:
            self.log.error('Monitoring exists. IMA could not store the slice monitoring. ')
            return False
        
        try:
            
            self.e2eActiveAdaptors[e2eAdaptorID] = data
            self.log.debug('Success to store new slice monitoring')
            return True
        
        except Exception as e:
            self.log.error('IMA could not store a new slice monitoring. Check the given parameters.')
            return (False, e)                                    

    def _list(self):
        return self.e2eActiveAdaptors
        
    def _update(self, uuid=None, data={}):
        e2eAdaptorID = uuid
        
        if not self._checkParams(e2eAdaptorID, data):    
            self.log.debug('Failed to update. None values. Check the given parameters.')
            return False
        
        if e2eAdaptorID not in self.e2eActiveAdaptors:
            self.log.error('Monitoring does not exists. IMA could not store the slice monitoring. ')
            return False
        
        try:
            self.e2eActiveAdaptors[e2eAdaptorID] = data
            self.log.debug(self.e2eActiveAdaptors)
            return True
        
        except Exception as e:
            return (False, e)
        
    def updateMonitoringInstanceId(self, uuid, data):
        e2eAdaptorID = uuid
        
        if e2eAdaptorID not in self.e2eActiveAdaptors:
            self.log.error('Monitoring does not exists. IMA could not store the slice monitoring. ')
            return False
        
        #print(dir(data))
        #self.e2eActiveAdaptors[e2eAdaptorID]['monitoring_instance'] = data
        self.instances.append(data)
        return True
        
    def listInstances(self):
        return self.instances
    
    def deleteInstance(self, instance):
        self.instances.remove(instance)
        
        
    def _delete(self, uuid=None):
        e2eAdaptorID = uuid   
        
        if uuid == None:
            self.log.debug('Failed to delete. None values. Check the given parameters.')
            return False
        
        try:
            del self.e2eActiveAdaptors[e2eAdaptorID]
            return True
        except KeyError as e:
            #print(dir(e))
            self.log.error('Monitoring does not exists. IMA could not delete the slice monitoring. ')
            return False, e
            
            
#Tests
#a = DSManagement()
        

