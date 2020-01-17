#!/usr/bin/env python
import pika
import json
from datetime import datetime
dt = datetime.now()


BINDING_KEY ='notice'
EXCHANGE_NAME='amq.topic'

rabbit_port = 5672
rabbit_host = 'localhost'
rabbit_user ='user'
rabbit_password ='password'
virtual_host = '/'
routing_key = BINDING_KEY
#msg ="Hello World!"
millisecond = dt.microsecond
msg = json.dumps( {"message":"Hello Message!","date":millisecond})




credentials = pika.PlainCredentials(rabbit_user,rabbit_password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(rabbit_host,rabbit_port,'/',credentials))
channel = connection.channel()

channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=routing_key, body=msg)
print(" [x] Sent ",msg)
connection.close()
