
import requests
import time
import datetime

#PROMETHEUS_SERVER = '10.7.229.183:9090/'
#PROMETHEUS_SERVER = 'http://demo.robustperception.io:9090/'
#PROMETHEUS_API = PROMETHEUS_SERVER + '/api/v1/query'


class PrometheusWrapper(object):
    
    def __init__(self, **kwargs):
        
        self.PROMETHEUS_SERVER = 'http://demo.robustperception.io:9090/'
        #self.PROMETHEUS_SERVER = 'http://10.7.229.183:9090/'
        self.PROMETHEUS_API = self.PROMETHEUS_SERVER + '/api/v1/query' 
        
    def runQuery(self, query):
        
        response = requests.post(self.PROMETHEUS_API,
                                params={
                                    'query': query
                                })
        results = response.json()['data']['result']
        return results
            
class Translate(object):

    def __init__(self, results, **kwargs):
        self.queryResults = results
        
    def to_dictSRO(self):
        pass
        
    
        
        
            


#a = PrometheusWrapper()
#query = 'node_memory_MemFree_bytes'
#results = a.makeQuery(query)    
#print(results)
#for result in results:
#    print(result['value'])
    #print(' {metric}: {value[1]}'.format(**result))

    
        