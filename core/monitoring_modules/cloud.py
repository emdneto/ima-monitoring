import time
from core.monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper
#from monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper

'''
Metrics: CPU, Memory and Bandwidth
'''

class CloudMonitoring(object):
    def __init__(self, slps):
        self.slps = slps
        self.prometheus = PrometheusWrapper()
    
    #especificar o job exemplo:{job="cloud-slice-monitor"}
    def CloudMonitoringCollector(self, slps):
      instances = []
      for slp in slps:
        instances.append(slp['dc_address']+':9100')
      metrics_per_instance = {}
      metrics_per_instance['slice_parts'] = {}

#      instances = ['demo.robustperception.io:9100']
      for instance in instances:
        instance_str = ("instance='" + instance + "'")
        query = "(100 - (avg by (instance) (irate(node_cpu_seconds_total{mode='idle'," + instance_str + "}[5m])) * 100)) or ((node_memory_MemTotal_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_MemFree_bytes{" + instance_str + "}))/1024/1024) or sum(rate(node_network_transmit_bytes_total{" + instance_str + "}[1m])/1024/1024) or rate(node_disk_read_bytes_total{"+ instance_str +"}[1m])"
        results = self.prometheus.runQuery(query)
        metrics_per_instance['slice_parts'][instance] = results
      
      for i in metrics_per_instance['slice_parts']:
        if len(metrics_per_instance['slice_parts'][i]) > 0:
          for a in (metrics_per_instance['slice_parts'][i]):
            if metrics_per_instance['slice_parts'][i].index(a) == 0:
              cpu = ({'cpu': a['value'][1]})
            elif metrics_per_instance['slice_parts'][i].index(a) == 1:
              mem_used = ({'memory_used': a['value'][1]})
            elif metrics_per_instance['slice_parts'][i].index(a) == 2:
              tx = ({'bandwidth_tx': a['value'][1]})
            elif metrics_per_instance['slice_parts'][i].index(a) == 3:
              disk_read = ({'disk_read': a['value'][1]})
          z = dict(list(cpu.items()) + list(mem_used.items()) + list(tx.items()) + list(disk_read.items()))
          metrics_per_instance['slice_parts'].update({i: z})

      for unit in instances:
        for mslp in slps:
          if (unit) == (mslp['dc_address']+":9100"):
            mslp['metrics'] = {}
            mslp['metrics'] = metrics_per_instance['slice_parts'][unit]
        
      return slps

    def _buildQuery(self):
        CPU = "100 - (avg by (instance) (irate(node_cpu_seconds_total{job='cloud_slice_monitor',mode='idle'[5m]})) * 100)"
        Mem_usage = "node_memory_MemTotal_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_MemFree_bytes{job='cloud_slice_monitor'})"
        TX="sum(rate(node_network_receive_bytes_total[1m])/1024/1024)"
        RX="sum(rate(node_network_transmit_bytes_total[1m]))/1024/1024"
        DISK_IN = 'rate(node_disk_read_bytes_total[1m])'
        DISK_OUT = 'rate(node_disk_written_bytes_total[1m])'

#exemplo = CloudMonitoring(" ")
#results = exemplo.CloudMonitoringCollector()
#print(results)
