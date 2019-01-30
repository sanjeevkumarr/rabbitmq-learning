import pika
import  sys



class Producer:



    message = {"interface" : "10.128.0.1","id":0}


    def send(self):

        Producer.message  = ''.join(sys.argv[1:]) or Producer.message

        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='interface_runner',durable=True)
            self.channel.basic_publish(exchange='' ,routing_key='interface_runner', body=str(Producer.message))
        except Exception as e:
            print("Exception while send message" +  str(e))
        finally:
            self.connection.close()

        print("Message sent successfully..." )
        print("send data")

producer = Producer()
producer.send()





