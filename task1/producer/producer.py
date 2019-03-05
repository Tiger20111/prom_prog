#!/usr/bin/env python
import pika
import logging
import sys
import random
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

queue_name = 'random_numbers'

conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue=queue_name)

logging.info("Waiting for logs. To exit press CTRL+C")

while True:
    number = random.randint(1, 100)
    logging.info("Producer sent number {}".format(number))

    channel.basic_publish(
        exchange='', routing_key=queue_name, body=str(number))

    time.sleep(random.randint(1, 5))

logging.info('closing connection')
connection.close()

