import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Connect to the local RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Subscribe to the queue
channel.basic_consume(queue='testPika',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
