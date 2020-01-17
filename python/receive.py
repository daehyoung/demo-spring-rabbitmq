#!/usr/bin/env python
import pika


BINDING_KEY ='notice'
EXCHANGE_NAME='amq.topic'

rabbit_port = 5672
rabbit_host = 'localhost' 
rabbit_user ='user' 
rabbit_password ='password'
virtual_host = '/'
binding_key = BINDING_KEY

credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
parameters = pika.ConnectionParameters(rabbit_host,
                                       rabbit_port,
                                       virtual_host,
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind( exchange=EXCHANGE_NAME,queue=queue_name,routing_key=binding_key)
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
