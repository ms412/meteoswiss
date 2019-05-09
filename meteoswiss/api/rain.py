
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class rain(object):

    def __init__(self):
        print(rain)
        _classLogger.debug('TTTTTT')

    def forcastRain(self,stationId):
        rainList = {}
        t = {}
        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for x in response:
            _tempList = (x['rainfall'])
            for y in _tempList:
                t[y[0]] = {'exp': y[1]}
               # t[]

        for x in response:
            _tempList = (x['variance_rain'])
            for y in _tempList:
                value = t[y[0]]
                value['min'] = y[1]
                value['max'] = y[2]
                t[y[0]] = value


            #    t['predicted'] = y[1]
          #  rainList = rainList + _tempList

        print(json.dumps(t,ensure_ascii=False))
        return t


