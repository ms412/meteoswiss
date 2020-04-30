
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class rain(object):

    def __init__(self):
        print(rain)
        _classLogger.debug('TTTTTT')

    def rainForcastToday(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
        response = self.getAPIcall(url)

        list = response[0]
        rainfall = (list['rainfall'])
        variance = (list['variance_rain'])
        #    timestamp = (list['min_date'])

        for idx, val in enumerate(rainfall):
            exp = rainfall[idx][1]
            min = variance[idx][1]
            max = variance[idx][2]

            result[val[0]] = {'exp': exp, 'min': min, 'max': max}

#        print(json.dumps(result,ensure_ascii=False))
        return result

    def rainForcastWeek(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            rainfall = (list['rainfall'])
            variance = (list['variance_rain'])

            for idx, val in enumerate(rainfall):
                exp = rainfall[idx][1]
                min = variance[idx][1]
                max = variance[idx][2]

                result[val[0]] = {'exp' :exp, 'min' : min, 'max' :max}

        return result

    def rainCurrent(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
       # print('xx',url)
        response = self.getAPIcall(url)

        for list in response:
            result = list['rainfall'][-1]


        return result

    def rainHistory3d(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)

        rainfall = response['messwerte-niederschlag-10min']['days'][0]['data']

        for idx, val in enumerate(rainfall):
         #   print(idx, val[0], val[1], rainfall[idx][1])
            x = {'rain':val[1]}
            result[val[0]] = x

       # print(result)
      #  return json.dumps(result, ensure_ascii=False)
        return result

    def rainHistory1y(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
        # print(response)

        rainfall = response['messwerte-niederschlag-10min']['year'][0]['data']

        for idx, val in enumerate(rainfall):
            x = {'rain':val[1]}
            result[val[0]] = x
            #print(idx,windDir['data'][idx])
          #  print(idx, val[0], val[1], windSpeedGusts['data'][idx][1]) #, windDir['data'][idx][1])
        #    x = {'wind': val[1], 'gusts': windSpeedGusts['data'][idx][1]} #, 'dir': windDir['data'][idx][1]}
         #   result[val[0]] = x

         #print(result)
        #return json.dumps(result, ensure_ascii=False)
        return result
