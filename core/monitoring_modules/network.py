import time
from core.monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper

'''
Metrics: Bandwidth, packet loss, RX/TX
'''
class NetworkMonitoring(object):
    
    def __init__(self, slps):
        #self.e2eAdaptorId
        self.slps = slps
        self.prometheus = PrometheusWrapper()
    
    def NetworkMonitoringCollector(self):
        query = 'node_memory_MemFree_bytes'
        results = self.prometheus.runQuery(query)
        return results
    
    def _buildQuery(self):
        TX = "node_network_transmit_total{job='network-slice-monitor}"
    """ def NetworkMonitoringPublisher(self):
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
        print('parou') """