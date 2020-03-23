
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class sunshine(object):


    def sunforcastyHour(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
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

    def sunforcastByDay(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
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

    def sunCurrent(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
      #  print('xx',url)
        response = self.getAPIcall(url)


        for list in response:
            result = list['sunshine'][-1]

        return result


    def sunRiseForcast5Days(self,stationId):

        result = {}

        url = self.getStationDetails(stationId)
        response = self.getAPIcall(url)

       # print(response['graph']['sunset'])
        return response['graph']['sunset']

    def sunSetForcast5Days(self,stationId):

        result = {}

        url = self.getStationDetails(stationId)
        response = self.getAPIcall(url)

       # print(response['graph']['sunrise'])
        return response['graph']['sunrise']

    def sunHistorical(self,stationId):

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

    def sunLast3Days(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        sunshine = response['messwerte-sonnenscheindauer-10min']['days'][0]['data']

        for idx, val in enumerate(sunshine):
          #  print(idx, val[0], val[1], qnh[idx][1], qff[idx][1], hpaA[idx][1], hpaB[idx][1])
            x = {'min':val[1]}
            result[val[0]] = x

        print(json.dumps(result, ensure_ascii=False))
        return result

    def sunLastYear(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        sunshine = response['messwerte-sonnenscheindauer-10min']['year'][0]['data']

        for idx, val in enumerate(sunshine):
          #  print(idx, val[0], val[1], qnh[idx][1], qff[idx][1], hpaA[idx][1], hpaB[idx][1])
            x = {'min':val[1]}
            result[val[0]] = x

        print(json.dumps(result, ensure_ascii=False))
        return result