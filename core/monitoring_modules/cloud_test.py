import time
#from core.monitoring_modules.utils.prometheus_wrapper import PrometheusWrapper
from utils.prometheus_wrapper import PrometheusWrapper

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
        TX="rate(node_network_transmit_bytes_total[1m])/1024/1024"
        RX="rate(node_network_receive_bytes_total[1m])/1024/1024"
        DISK_IN = 'rate(node_disk_read_bytes_total[1m])'
        DISK_OUT = 'rate(node_disk_written_bytes_total[1m])'


slps_dc = [{'type': 'DC', 'slice_part_name': 'core-dc-public', 'dc_address': 'demo.robustperception.io', 'slice_part_id': 1, 'location': 'natal', 'vdus': [{'name': 'core-vm', 'ip_address': '166.172.78.230', 'mac_address': '02: 00: 00: 9d:f5:f3', 'id': 1}]}, {'type': 'DC', 'slice_part_name': 'core-dc-private', 'dc_address': '10.7.229.92', 'slice_part_id': 3, 'location': 'natal', 'vdus': [{'name': 'core-vm', 'ip_address': '107.199.197.230', 'mac_address': '02: 00: 00: 62:ca: 7a', 'id': 3}]}]
exemplo = CloudMonitoring(slps_dc)
results = exemplo.CloudMonitoringCollector(slps_dc)
print (results)