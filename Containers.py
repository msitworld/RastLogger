from Services.ConfigService import ConfigService
from Services.InventoryEventService import InventoryEventService
from Services.RabbitMQService import RabbitMQService
from Data.MongoContext import MongoContext

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import os

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')

class ConfigServices(containers.DeclarativeContainer):
    url = os.environ['CONFIG_URL']
    #url = 'http://192.168.13.201:8050/api/config/get'
    print(F"Reading configs from: {url} ...")
    configService = providers.Singleton(ConfigService, url=url)

class MongoContexts(containers.DeclarativeContainer):
    mongoContext = providers.Singleton(MongoContext, connectionString=ConfigServices.configService().Get('v:rast:connectionstring'))

class InventoryEventServices(containers.DeclarativeContainer):
    inventoryEventService = providers.Factory(InventoryEventService, context=MongoContexts.mongoContext)

class RabbitMQServices(containers.DeclarativeContainer):
    rabbitMQService = providers.Singleton(RabbitMQService, config=ConfigServices.configService)