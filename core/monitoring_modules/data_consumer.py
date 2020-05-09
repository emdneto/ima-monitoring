import pika
import sys
import time
import threading
import logging
from core.monitoring_modules.network import NetworkMonitoring

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
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
        self.sliceData = data
        #self.e2eAdaptorId = data['e2eAdaptor_instance_id']
        self.e2eAdaptorActive = True
        thread = threading.Thread(target=self.startMonitors, args=())
        thread.daemon = True
        thread.start()

# TO DO: Colocar essas funções p/ executarem de forma assíncrona (asyncio).        
    def startMonitors(self):
        slps = {}        
        e2eAdaptorId = self.sliceData['e2eAdaptor_instance_id']
        slice_parts = self.sliceData['slice_parts']
        
        #slps['NET'] = []
        #slps['DC'] = []
        #slps['EDGE'] = []
        #slps['WIFI'] = []
        

        for slice_part in slice_parts:
            slp_type = slice_part['type']
            try:
                slps[slp_type].append(slice_part)    
            except Exception as identifier:
                slps[slp_type] = []
                slps[slp_type].append(slice_part)
            #slps[slp_type][]
            
            

        print(slps)

            
        
        #net = NetworkMonitoring(slps['NET'])
        #edge = EdgeMonitoring(slps['EDGE'])
        #dc = CloudMonitoring(slps['DC'])
        #wifi = WifiMonitoring(slps['WIFI'])
        
        i = 0
        while self.e2eAdaptorActive:
            #network_metrics = net.NetworkMonitoringCollector()
            #edge_metrics = edge.EdgeMonitoringCollector()
            #dc_metrics 
            #message = str(self.e2eAdaptorId) + ' - Message' + str(i) +  ' ' + str(network_metrics)
            #channel.basic_publish(exchange='metrics', routing_key=str(self.e2eAdaptorId), body=message)
            
            message = str(e2eAdaptorId) + ' - Message ' + str(i)
            print(slps['DC'])
            print(" [x] Sent %r" % message)
            #channel.basic_publish(exchange='metrics', routing_key=str(self.e2eAdaptorId), body=slice_data)
            time.sleep(5)
            i += 1
        #channel.close()
        print('parou') 

        
        
        
        

        
        #self.connection = pika.
        
    
        