import pika
import sys
import time
import threading
import logging
from core.monitoring_modules.network import NetworkMonitoring
from core.monitoring_modules.cloud import CloudMonitoring
from core.monitoring_modules.edge import EdgeMonitoring
#from monitoring_modules.network import NetworkMonitoring
#from monitoring_modules.cloud import CloudMonitoring

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
#        print (e2eAdaptorId) 
        slps['NET'] = []
        slps['DC'] = []
        slps['EDGE'] = []
        slps['WIFI'] = []



        for type_slp in slice_parts:
            for slice_part in (slice_parts[type_slp]):
                if type_slp == 'pcpe':
                    slp_type = (slice_part['type'])
                else:
                    slp_type = (slice_part['type'])
                try:
                    slps[slp_type].append(slice_part)    
                except Exception as identifier:
                    slps[slp_type] = []
                    slps[slp_type].append(slice_part)
                #slps[slp_type][]


        print (slps)
                 
        if len(slps['NET']) != 0:
          net = NetworkMonitoring(slps['NET'])
        if len(slps['EDGE']) != 0:
          edge = EdgeMonitoring(slps['EDGE'])
        if len(slps['DC']) != 0:
          dc = CloudMonitoring(slps['DC'])
        if len(slps['WIFI']) != 0:
          wifi = WifiMonitoring(slps['WIFI'])

        i = 0
        while self.e2eAdaptorActive:
            if len(slps['NET']) != 0:
                network_metrics = net.NetworkMonitoringCollector()
            if len(slps['EDGE']) != 0:
                edge_metrics = edge.EdgeMonitoringCollector()
            if len(slps['DC']) != 0:
                dc_metrics = dc.CloudMonitoringCollector()
            #if len(slps['WIFI']) != 0:
            #    wifi_metrics = wifi.WifiMonitoringCollector()
            #print (dc_metrics)
            #message = str(self.e2eAdaptorId) + ' - Message' + str(i) +  ' ' + str(network_metrics)
            #channel.basic_publish(exchange='metrics', routing_key=str(self.e2eAdaptorId), body=message)
            
            message = str(e2eAdaptorId) + ' - Message ' + str(i)
            #print(slps['DC'])
            print(" [x] Sent %r" % message)
            #channel.basic_publish(exchange='metrics', routing_key=str(self.e2eAdaptorId), body=slice_data)
            time.sleep(5)
            i += 1
        #channel.close()
        print('parou') 

         
#        slps = {"slice_id": 5,"slice_name": "Fon_Slices","slice_parts": [{"slice_part_id": 157,"slice_part_name": "Fon_slices_Cloud","type": "DC","vdus": []},{"slice_part_id": 1050,"slice_part_name": "Fon_slice_Edge","type": "EDGE","vdus": []},{"slice_part_id": 8005,"slice_part_name": "Fon_slice_Network","type": "NET","vdus": [],"bridges": [],"ports": []}]}


#        a = Monitoring()
#        print (a)

    '''        for slp_edge in (slice_parts["edge"]):
#           print (slp_edge['type'])
            slp_type = slp_edge['type']
            try:
                slps[slp_type].append(slp_edge)    
            except Exception as identifier:
                slps[slp_type] = []
                slps[slp_type].append(slp_edge)
        for slp_pcpe in (slice_parts["pcpe"]):
#           print (slp_pcpe['type'])
            slp_type = slp_pcpe['type']
            try:
                slps[slp_type].append(slp_pcpe)    
            except Exception as identifier:
                slps[slp_type] = []
                slps[slp_type].append(slp_pcpe)'''

'''        for slice_part in slice_parts:
            slp_type = slice_part['type']
            try:
                slps[slp_type].append(slice_part)    
            except Exception as identifier:
                slps[slp_type] = []
                slps[slp_type].append(slice_part)
            #slps[slp_type][]'''


