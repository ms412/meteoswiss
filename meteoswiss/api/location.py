

import requests
from lxml import html
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class location(base.apiClient):

    def getStationByAreaCode(self,plz):
        result = []
        _plz = str(plz)[:2]

        response = self.getAPIcall('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/%s.json'%_plz)

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

        response = self.getAPIcall('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/%s.json' % _name)

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

        response = self.getAPIcall('https://www.meteosuisse.admin.ch/etc/designs/meteoswiss/ajax/location/%s.json' % stationId)

        if not response:
            _classLogger.error('cannot find Station by Id; StationId: %s' % stationId)
            return False

        _classLogger.debug('Station found%s' % response)
        return response

    def getStationPrediction(self):
        #        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get('https://www.meteosvizzera.admin.ch/home.html')
        tree = html.fromstring(page.content)
        print('Tree',tree)
        # This will create a list of buyers:
        buyers = tree.xpath('//div[@title="buyer-name"]/text()')
        #        doc.xpath("//div[@class='channel-title-container']")
        # This will create a list of prices
        prices = tree.xpath('//span[@class="item-price"]/text()')
        test = tree.xpath('//div[@class ="overview__local-forecast clearfix"][data-json-url]')
        print('xx',test)
        for item in test:
            print(item)
        print(test)
        print(buyers)
        print(prices)
        for item in tree.xpath("//div"):
            #   print(item)
            for classname in iter(item.classes):
                if classname == "overview__local-forecast":
                    print(classname)
                    print(classname['data-json-url'].text)