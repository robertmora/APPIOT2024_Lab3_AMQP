import pika

# Connect to the local RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message_body = 'APPIOT 2024'

# Send a message to the 'testPika' queue
channel.basic_publish(exchange='',
                      routing_key='testPika',
                      body=message_body)
print(f"Sent message: {message_body}")


# Close the connection
connection.close()
