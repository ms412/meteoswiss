
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class temperature(object):

    def forcastTemperatureByHour(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
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

        url = self.getPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            temperature = (list['temperature'])
            variance = (list['variance_range'])
            timestamp = (list['min_date'])

            min =0
            max = 0
            for idx, val in enumerate(temperature):
             #   exp = exp + temperature[idx][1]
              #  print(idx)
                if idx == 0:
                    min = variance[idx][1]
                    max = variance[idx][2]
            #        print('idx',idx)

                if min >  variance[idx][1]:
                    min =  variance[idx][1]


                if max <  variance[idx][2]:
                    max =  variance[idx][2]

             #   print(idx,min, max)


            result[timestamp] = {'min' : min, 'max' :max}

       # print(json.dumps(result, ensure_ascii=False))

        return result

    def currentTemperature(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
        print('xx',url)
        response = self.getAPIcall(url)

        for list in response:
            result = list['temperature'][-1]

        return result