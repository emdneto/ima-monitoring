#!/usr/bin/env python3.7

import pika
import sys
import logging
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='metrics', exchange_type='fanout')

result = channel.queue_declare(queue='3', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='metrics', queue=queue_name)

print(' [*] Waiting for metrics. To exit press CTRL+C')

def callback(ch, method, properties, body):
    ss = (" [x] %s" % body)
    print (ss)
    path = 'metrics.txt'
    metric_file = open(path,'w')
    metric_file.write(ss)  

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

a = channel.start_consuming()
path = 'metrics.txt'
metric_file = open(path,'w')
metric_file.write(a)
