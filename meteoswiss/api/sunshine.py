
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class sunshine(object):


    def forcastSunshineByHour(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            sunshine = (list['sunshine'])
         #   variance = (list['variance_rain'])
            timestamp = (list['min_date'])

            for idx, val in enumerate(sunshine):
                exp = sunshine[idx][1]
           #     min = variance[idx][1]
            #    max = variance[idx][2]

                result[val[0]] = {'exp': exp}

#        print(json.dumps(result,ensure_ascii=False))
        return result

    def forcastSunshineByDay(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            sunshine = (list['sunshine'])
         #   variance = (list['variance_rain'])
            timestamp = (list['min_date'])

            exp = 0
       #     min = 0
        #    max = 0
            for idx, val in enumerate(sunshine):
                exp = exp + sunshine[idx][1]
              #  min = min + variance[idx][1]
               # max = max + variance[idx][2]

            result[timestamp] = {'exp' :exp}

     #   print(json.dumps(result, ensure_ascii=False))

        return result

    def currentSunshine(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
      #  print('xx',url)
        response = self.getAPIcall(url)

        for list in response:
            result = list['sunshine'][-1]

        return result


    def getSunset(self,stationId):

        result = {}

        url = self.getDetails(stationId)
        response = self.getAPIcall(url)

        print(response['graph']['sunset'])
        return

    def getSunrise(self,stationId):

        result = {}

        url = self.getDetails(stationId)
        response = self.getAPIcall(url)

        print(response['graph']['sunrise'])
        return

    def historicalSunshine(self,stationId):

        result = {}

        url = self.getMeasurement(stationId)
        response = self.getAPIcall(url)

        for list in response:
            sunshine = (list['sunshine'])
            #   variance = (list['variance_rain'])
           # timestamp = (list['min_date'])

           # exp = 0
            #     min = 0
            #    max = 0
            for idx, val in enumerate(sunshine):
                result[sunshine[idx][0]] = sunshine[idx][1]

             #   exp = exp + sunshine[idx][1]
            #  min = min + variance[idx][1]
            # max = max + variance[idx][2]

         #   result[timestamp] = {'exp': exp}
        return result