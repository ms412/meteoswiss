
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

    def getStationByName(self,name):
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

    def getMeasurementStation(self,stationId):

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

      #  print(path)
       # print(self._url + path.replace('800100',str(stationId),1))

        return self._url + path.replace('800100',str(stationId),1)

    def getStationMeasurement(self,station='BER'):
       # print(stationId)
        #        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get(self._url)
        tree = html.fromstring(page.content)

        response = tree.xpath('//div[@class="overview__local-forecast clearfix"]')
        path = (response[0].attrib['data-measurements-json-url'])

       # print(path)
      #  print(self._url + path.replace('SMA',station,1))
        return self._url + path.replace('SMA',station,1)



    def getDetails(self,stationId='800100'):

     #   path = ('/etc/designs/meteoswiss/ajax/location/{}.json'.format(stationId))

        path = ('https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz={}'.format(stationId))

        return path

    def getMeasurement(self,stationId='800100'):
      #  /etc/designs/meteoswiss/ajax/location/305200.json
      #/product/output/measured-values/homepage/version__20190512_0642/fr/GVE.json" data-measurements-json-url
        response = self.getMeasurementStation(stationId)
        station = response['station_id']

        url = self.getStationMeasurement(station)
      #  print('cc',url)

      #  response = self.getAPIcall(url)
     #   print(response)
        return url

    def getMeasurementV3(self,stationId='800100'):
        mesurementData = {}
        page = requests.get(self._url + '/home/messwerte.html')
        tree = html.fromstring(page.content)

        result = tree.get_element_by_id('measurementv3-dataview-tmpl')
       # print(type(result))
        _html= result.text_content().encode('utf-8')
        _html = _html.decode("utf-8")

        regex="\/product\/output\/measured-values-v3\/map\/version__[0-9]{6,8}_[0-9]{2,4}/en/chartPaths.json"

        result = re.search(regex,_html)

        if result:
            path = result.group(0)

            station_id = self.getMeasurementStation(stationId)['station_id']
            response = self.getAPIcall(self._url + path)['params']

          #  mesurementData['measurementStation'] = response
            for key1, item1 in response.items():
               # print(key1)
                dictTemp = {}
                for key2, path in item1.items():

                    path = path.replace('% selection.station %',station_id,1)
                   # print('path',path)
                   # print(key2, path)
                    response = self.getAPIcall(self._url + path)['series']
                    dictTemp[key2] = response
                    #print(dictTemp)

                mesurementData[key1]= dictTemp
               # print('x',mesurementData)
           # print(response)
       # print(json.dumps(result, ensure_ascii=False))
        return json.dumps(mesurementData, ensure_ascii=False)



