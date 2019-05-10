
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class temperature(object):

    def forcastTemperatureByHour(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            temperature = (list['temperature'])
            variance = (list['variance_range'])
            timestamp = (list['min_date'])

            for idx, val in enumerate(temperature):
                exp = temperature[idx][1]
                min = variance[idx][1]
                max = variance[idx][2]

                result[val[0]] = {'exp': exp, 'min': min, 'max': max}

#        print(json.dumps(result,ensure_ascii=False))
        return result

    def forcastTemperatureByDay(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            temperauter = (list['temperature'])
            variance = (list['variance_range'])
            timestamp = (list['min_date'])

            exp = 0
            min = 0
            max = 0
            for idx, val in enumerate(temperature):
                exp = exp + temperature[idx][1]
                min = min + variance[idx][1]
                max = max + variance[idx][2]

            result[timestamp] = {'exp' :exp, 'min' : min, 'max' :max}

     #   print(json.dumps(result, ensure_ascii=False))

        return result
