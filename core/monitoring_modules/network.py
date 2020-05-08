import time
class NetworkMonitoring(object):
    
    def __init__(self, e2eData, conn):
        super().__init__()
        self.shouldPublish = True
        self.e2eAdaptorId
    
    def NetworkMonitoringCollector(self):
        pass
    
    def NetworkMonitoringPublisher(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange='metrics', exchange_type='fanout')
        
        i = 0
        while self.e2eAdaptorActive:
            message = str(self.e2eAdaptorId) + 'Message ' + str(i)
            channel.basic_publish(exchange='metrics', routing_key=str(self.e2eAdaptorId), body=message)
            print(" [x] Sent %r" % message)
            time.sleep(5)
            i += 1
        channel.close()
        print('parou')