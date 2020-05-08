#!/usr/bin/env python3.7

import pika
import sys
import logging
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

result = channel.queue_declare(queue='3', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='metrics', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %s" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()