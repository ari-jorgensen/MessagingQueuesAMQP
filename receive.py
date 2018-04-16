import pika

# Create connection - similar to socket.bind()
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# Joining queue
channel.queue_declare(queue='hello')

# Function that handles received messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Will wait for message in specified queue
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
