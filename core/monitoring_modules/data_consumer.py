import pika
import sys
import time
import threading
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
class SROConsumerInterface(object):
    
    def __init__(self):
        pass

class PikaConnection(object):
    
    _pikaInstance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._pikaInstance is None:
            cls._pikaInstance = super(PikaConnection, cls).__new__(cls)
        
        return cls._pikaInstance
    
    def __init__(self):
        self.log = logging.getLogger("PikaConnection")
        
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        except Exception as e:
            self.log.error('Failed to connect Rabbitmq server')
        
        #self.channel = self.connection.channel()
       
        
class Monitoring(PikaConnection):
    
    def __init__(self, data={}):
        super().__init__()
        self.log = logging.getLogger("Monitoring")
        self.e2eAdaptorID = data['e2eAdaptor_instance_id']
        self.e2eAdaptorActive = True
        thread = threading.Thread(target=self.startMonitor, args=())
        thread.daemon = True
        thread.start()
        #thread.join()
        #self.startNetworkMonitor()
        
    def startMonitor(self):
        self.startNetworkMonitor()
        
        
        
        
        

        
        #self.connection = pika.
        
    
        