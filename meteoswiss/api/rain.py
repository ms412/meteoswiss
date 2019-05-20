
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class rain(object):

    def __init__(self):
        print(rain)
        _classLogger.debug('TTTTTT')

    def forcastRainByHour(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            rainfall = (list['rainfall'])
            variance = (list['variance_rain'])
            timestamp = (list['min_date'])

            for idx, val in enumerate(rainfall):
                exp = rainfall[idx][1]
                min = variance[idx][1]
                max = variance[idx][2]

                result[val[0]] = {'exp': exp, 'min': min, 'max': max}

#        print(json.dumps(result,ensure_ascii=False))
        return result

    def forcastRainByDay(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            rainfall = (list['rainfall'])
            variance = (list['variance_rain'])
            timestamp = (list['min_date'])

            exp = 0
            min = 0
            max = 0
            for idx, val in enumerate(rainfall):
                exp = exp + rainfall[idx][1]
                min = min + variance[idx][1]
                max = max + variance[idx][2]

            result[timestamp] = {'exp' :exp, 'min' : min, 'max' :max}

     #   print(json.dumps(result, ensure_ascii=False))

        return result

    def currentRainfall(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
       # print('xx',url)
        response = self.getAPIcall(url)

        for list in response:
            result = list['rainfall'][-1]


        return result