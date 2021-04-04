import pika


class Consumer():

    def _init_channel(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters('amqps://ugbppmle:1KV3dQQTVZEUtQmh1sMhEepDP6IFXgXt@hornet.rmq.cloudamqp.com/ugbppmle')
        )
        self.channel = self.connection.channel()

        return self.channel

    def _init_queue(self, exchange, queue_name, routing_key):
        self.queue = self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(
            exchange=exchange,
            queue=queue_name,
            routing_key=routing_key
        )
        return queue_name

    def consume(self, exchange, queue_name, routing_key, callback):
        channel = self._init_channel()
        queue_name = self._init_queue(exchange, queue_name, routing_key)
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )
        channel.start_consuming()
        channel.close()

consumer = Consumer()
