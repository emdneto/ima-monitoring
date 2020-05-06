import pika
import sys
import time
import threading

class SROConsumerInterface(object):
    
    def __init__(self):
        pass
        
        
class PikaConnection():

    def __init__(self):
        super().__init__()
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        #self.channel = self.connection.channel()

    def pikaCloseConnection(self):
        self.connection.close()
        
        
        
class Monitoring(PikaConnection):
    
    def __init__(self, data={}):
        super().__init__()
        self.e2eAdaptorID = data['e2eAdaptor_instance_id']
        self.e2eAdaptorActive = True
        thread = threading.Thread(target=self.startNetworkMonitor, args=())
        thread.daemon = True
        thread.start()
        thread.join()
        #self.startNetworkMonitor()
        
    def startNetworkMonitor(self):
        #self.channel.exchange_declare(exchange='metrics', exchange_type='fanout')
        i = 0
        while self.e2eAdaptorActive:
            message = 'Message ' + str(i)
            print(message)
            time.sleep(5)
            i += 1
        

        
        #self.connection = pika.
        
    
        