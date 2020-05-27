import time
from core.monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper
#from monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper

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
        CPU = "100 - (avg by (instance) (irate(node_cpu_seconds_total{job='network_slice_monitor',mode='idle'[5m]})) * 100)"
        Mem_usage = "node_memory_MemTotal_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_MemFree_bytes{job='network_slice_monitor'})"
        RX="rate(node_network_receive_bytes_total[1m])/1024/1024"
        DISK_IN = 'rate(node_disk_read_bytes_total[1m])'
        DISK_OUT = 'rate(node_disk_written_bytes_total[1m])'

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

#exemplo = NetworkMonitoring(" ")
#results = exemplo.NetworkMonitoringCollector()
#print(results)

