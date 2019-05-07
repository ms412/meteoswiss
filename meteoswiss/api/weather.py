
import requests
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class weather(base.apiClient):

    def __init__(self):
        print('weather Test')

    def getStation(self,plz):
        result = requests.get('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/3.json')
        print(result)
        _classLogger.debug('getStation')
        result = self.getCall('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/3.json')