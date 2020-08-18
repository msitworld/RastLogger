from Subscribers.EventSubscriber import EventSubscriber
from Containers import RabbitMQServices, InventoryEventServices

if __name__ == '__main__':

    print(' [*] Waiting for logs. To exit press CTRL+C')

    EventSubscriber(InventoryEventServices.inventoryEventService(), 
    RabbitMQServices.rabbitMQService()
    ).Run()