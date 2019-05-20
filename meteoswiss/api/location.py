
import re
import json
import requests
from lxml import html, etree
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class location(base.apiClient):

    def __init__(self):
        self._url = 'https://www.meteoswiss.admin.ch'

    def getStationByAreaCode(self,plz):
        result = []
        _plz = str(plz)[:2]

        path = ('/etc/designs/meteoswiss/ajax/search/{}.json'.format(_plz))

        response = self.getAPIcall(self._url + path)

        if not response:
            _classLogger.error('cannot find Station')
            return False

        for x in response:
            z = x.split(';')
            if str(plz) in z[3]:
                result.append(z[0])

        _classLogger.debug('Station found %s'% result)
        return result

    def getStationByVillage(self,name):
        result = []
        _name = name.lower()[:2]

        path = ('/etc/designs/meteoswiss/ajax/search/{}.json'.format(_name))

        response = self.getAPIcall(self._url + path)

        if not response:
            _classLogger.error('cannot find Station')
            return False
       # print(response)
        for x in response:
            z = x.split(';')
            #if name.lower() in z[5].lower():
            for s in z:
              #  print(name.lower(),s.lower())
                if name.lower() == s.lower():
           #         print('found',s)
               # result.append(z[0])
                    result.append(z[0])

        _classLogger.debug('Station found %s' % result)
        return result

    def getStation(self,stationId):

        path = ('/etc/designs/meteoswiss/ajax/location/{}.json'.format (stationId))

        response = self.getAPIcall(self._url + path)

        if not response:
            _classLogger.error('cannot find Station by Id; StationId: %s' % stationId)
            return False

        _classLogger.debug('Station found%s' % response)
        return response

    def getStationDetails(self,stationId='800100'):

     #   path = ('/etc/designs/meteoswiss/ajax/location/{}.json'.format(stationId))

        path = ('https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz={}'.format(stationId))

        return path



