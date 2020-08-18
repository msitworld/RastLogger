import json

class EventSubscriber(object):

    def __init__(self, inventoryEventService, rabbitMQService):
        self.__inventoryEventService = inventoryEventService
        self.__rabbitMQService = rabbitMQService
    
    def callback(self, ch, method, properties, body):
        try:
            eventData = json.loads(body.lower())
            self.__inventoryEventService.AddEvent(eventData["id"], str(eventData["available"]).lower())
        except Exception as e:
            print(F"Exception at event subscriber callback: {str(e)}")

    def Run(self):

        rabbitMqExchangeName = 'gm.rast'
        rabbitMqQueueName = 'gm.rast.q'
        rabbitMQRoutingKey = 'gm.rast.productIsAvailable'

        self.__rabbitMQService.Start(
        rabbitMqExchangeName, 
        rabbitMqQueueName, 
        rabbitMQRoutingKey, 
        self.callback)
        