import os
import time
import re
import json
import requests
from lxml import html, etree
import logging
from bs4 import BeautifulSoup
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class measurement(base.apiClient):
    _storeDanger = {}
    _measuresHistorical = {}
    _prediction = {}

    def __init__(self):
        self._url = 'https://www.meteoswiss.admin.ch'

    def getPrediction(self,stationId='800100'):

        if self._prediction.get('UPDATE',0) + 600 > time.time():
            return self._prediction.get('DATA',False)

        else:

            page = requests.get(self._url)
            tree = html.fromstring(page.content)

            response = tree.xpath('//div[@class="overview__local-forecast clearfix"]')
            path = (response[0].attrib['data-json-url'])

            _data = self._url + path.replace('800100',str(stationId),1)

            self._prediction['DATA'] = _data

        self._prediction['UPDATE'] = time.time()

        return self._prediction['DATA']

    def getMeasurementByStationCode(self,station='BER'):
       # print(stationId)
        #        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get(self._url)
        tree = html.fromstring(page.content)

        response = tree.xpath('//div[@class="overview__local-forecast clearfix"]')
        path = (response[0].attrib['data-measurements-json-url'])

       # print(path)
      #  print(self._url + path.replace('SMA',station,1))
        return self._url + path.replace('SMA',station,1)

    def getMeasurement(self,stationId='800100'):
      #  /etc/designs/meteoswiss/ajax/location/305200.json
      #/product/output/measured-values/homepage/version__20190512_0642/fr/GVE.json" data-measurements-json-url
        response = self.getStation(stationId)
   #     print('bb',response)
        station = response['station_id']

        url = self.getMeasurementByStationCode(station)
      #  print('cc',url)

      #  response = self.getAPIcall(url)
     #   print(response)
        return url


    def getMeasurementV3(self,stationId='800100'):

        if self._measuresHistorical.get('UPDATE',0) + 600 > time.time():
          #  print('no update')
            return self._measuresHistorical.get('DATA',False)
        else:
           # print('update')
            #self._measuresHistorical['DATA'] ={}
            _page = requests.get(self._url + '/home/messwerte.html')
            soup = BeautifulSoup(_page.content,'lxml')

            _tag = soup.find(id="measurementv3-dataview-tmpl")

            _subtag = BeautifulSoup(_tag.string,'lxml')
            _content = _subtag.find(re.compile("measurementv3-detailview"))

            _path = _content['data-details-json']

            station_id = self.getStation(stationId)['station_id']
            response = self.getAPIcall(self._url + _path)['params']
      #      print(response)

            self._measuresHistorical['DATA'] = {}
            for _key1, _item1 in response.items():

            # print(key1)
                _dictTemp = {}
                for _key2, _path in _item1.items():
                    _path = _path.replace('% selection.station %', station_id, 1)
                    try:
                        response = self.getAPIcall(self._url + _path)['series']
                 #       print('get files',self._url + _path )
                    except:
                        print('Failed to get file from server %s',self._url + _path)
                        response = 0
                    _dictTemp[_key2] = response
             #       print(_key1)

                self._measuresHistorical['DATA'][_key1] = _dictTemp

        self._measuresHistorical['UPDATE'] = time.time()

        return self._measuresHistorical['DATA']


    def getWarnRegion(self,stationID='800100'):
        return self.getStation(stationID)['warn_region_ids']

    def getWarning(self,stationID='800100'):
        _page = requests.get(self._url + '/home.html?tab=alarm')
        soup = BeautifulSoup(_page.content, 'html.parser')
        _tag = (soup.find_all(id="dangers-map"))[0]
        _path = _tag['data-json-url']

        # if object is in store don't load again
        _storeFile = self._storeDanger.get('PATH',False)
        if _storeFile != _path:
            _data = self.getAPIcall(self._url + _path)
            self._storeDanger['PATH'] = _path
            self._storeDanger['DATA'] = _data
     #       print('load')
        else:
            _data = self._storeDanger['DATA']
     #       print('notload')

        return _data