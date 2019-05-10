

import requests
from lxml import html
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class location(base.apiClient):

    def __init__(self):
        self._url = 'https://www.meteoswiss.admin.ch'

    def getStationByAreaCode(self,plz):
        result = []
        plz = str(plz)[:2]

        path = ('/etc/designs/meteoswiss/ajax/search/{}.json'.format(plz))

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

    def getStationByName(self,name):
        result = []
        name = name.lower()[:2]

        path = ('/etc/designs/meteoswiss/ajax/search/{}.json'.format(name))

        response = self.getAPIcall(self._url + path)

        if not response:
            _classLogger.error('cannot find Station')
            return False

        for x in response:
            z = x.split(';')

            if name.lower() in z[5].lower():
                result.append(z[0])

        _classLogger.debug('Station found %s' % result)
        return result

    def getStationDetails(self,stationId):

        path = ('/etc/designs/meteoswiss/ajax/location/{}.json'.format (stationId))

        response = self.getAPIcall(self._url + path)

        if not response:
            _classLogger.error('cannot find Station by Id; StationId: %s' % stationId)
            return False

        _classLogger.debug('Station found%s' % response)
        return response

    def getStationPrediction(self,stationId='800100'):
        #        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get(self._url)
        tree = html.fromstring(page.content)

        response = tree.xpath('//div[@class="overview__local-forecast clearfix"]')
        path = (response[0].attrib['data-json-url'])


        return self._url + path.replace('800100',stationId,1)

    def getStationMeasurement(self,stationId='800100'):
        print(stationId)
        #        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get(self._url)
        tree = html.fromstring(page.content)

        response = tree.xpath('//div[@class="overview__local-forecast clearfix"]')
        path = (response[0].attrib['data-measurements-json-url'])

        print(path)
        return self._url + path.replace('800100',stationId,1)



