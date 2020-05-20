import time
from core.monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper
#from utils.prometheus_wrapper import PrometheusWrapper

'''
Metrics: CPU, Memory and Bandwidth
'''

class CloudMonitoring(object):
    def __init__(self, slps):
        self.slps = slps
        self.prometheus = PrometheusWrapper()

    def CloudMonitoringCollector(self):
#        query = 'node_memory_MemFree_bytes'
        query = "(100 - (avg by (instance) (irate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)) or ((node_memory_MemTotal_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_MemFree_bytes))/1024/1024)"
        results = self.prometheus.runQuery(query)
        return results

    def _buildQuery(self):
        CPU = "100 - (avg by (instance) (irate(node_cpu_seconds_total{job='cloud_slice_monitor',mode='idle'[5m]})) * 100)"
        Mem_usage = "node_memory_MemTotal_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_MemFree_bytes{job='cloud_slice_monitor'})"


exemplo = CloudMonitoring(" ")
results = exemplo.CloudMonitoringCollector()
print(results)
