from datetime import datetime
import pytz

class InventoryEventService(object):
    
    def __init__(self, context):
        self.__context = context
    
    def AddEvent(self, id, available):
        try:

            db = self.__context.GetCollection('rastdb')

            event = {
                'Id' : id,
                'Available' : available,
                'EventDate' : datetime.now(pytz.timezone('Iran'))
            }

            db.Event.insert_one(event)

            availablility = "Available" if available == "true" else "Unavailable"

            print(F"EventDate: {datetime.now(pytz.timezone('Iran')).strftime('%Y-%m-%d %H:%M')} | Product Id: {id} ===========> {availablility}")
            
        except Exception as e:
            print(F"Exception:{str(e)}")

