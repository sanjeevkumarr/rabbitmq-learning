import pika

import time

class Consumer:

    def callback(self, channel, method,properties,body):

        print("Consumer received the message ====> " + str(body))
        time.sleep(body.count(b'.'))
        print("Processed ====> ")
        channel.basic_ack(delivery_tag=method.delivery_tag)


    def receive(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare('interface_runner',durable=True)
        self.channel.basic_consume(self.callback,queue='interface_runner',no_ack=False)
        self.channel.basic_qos(prefetch_count=1)

        print("Will consume infinately")
        self.channel.start_consuming()


consume = Consumer()
consume.receive()








