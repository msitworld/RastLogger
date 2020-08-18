import pika

class RabbitMQService(object):

    def __init__(self, config):
        self.__config = config

    def Start(self, exchangeName, queueName, routingKey, callback):

        rabbitMqHost = self.__config.Get('v:rast:rabbitMQHost')
        rabbitMqUserName = self.__config.Get('v:rast:rabbitMQUserName')
        rabbitMqPassword = self.__config.Get('v:rast:rabbitMQPassword')
        
        rabbitMqExchangeName = exchangeName
        rabbitMqQueueName = queueName
        rabbitMQRoutingKey = routingKey

        credentials = pika.PlainCredentials(rabbitMqUserName, rabbitMqPassword)

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitMqHost, credentials=credentials))

        channel = connection.channel()

        channel.exchange_declare(exchange=rabbitMqExchangeName, exchange_type='topic', durable=True)

        result = channel.queue_declare(rabbitMqQueueName, durable=True)

        queue_name = result.method.queue

        channel.queue_bind(
            exchange=rabbitMqExchangeName, queue = queue_name, routing_key = rabbitMQRoutingKey)

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()
