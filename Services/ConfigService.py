import urllib.request
import json

class ConfigService(object):
    
    def __init__(self, url):
        self.__url = url

    def Get(self, key):
        try:

            body = urllib.request.urlopen(self.__url).read()
            
            configs = json.loads(body)

            for c in configs:
                if str(c['key']).lower() == str(key).lower():
                    return c['value']
                    
            print('The config key was not found!')

        except Exception as e:
            print(F"Exception at reading config keys: {str(e)}")
