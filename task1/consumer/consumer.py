#!/usr/bin/env python
import pika
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

queue_name = 'random_numbers'

conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    logging.info("Consumer gived number {}".format(body.decode("utf-8")))

channel.basic_consume(callback, queue=queue_name)

logging.info("Waiting for logs. To exit press CTRL+C")

while True:
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
 
logging.info('closing connection')
connection.close()
