
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class wind(object):

    def forcastWindByHour(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            wind = (list['wind']['data'])
            direction = (list['wind']['symbols'])

            for idx, val in enumerate(wind):
                force = wind[idx][1]
                if idx % 2: #ungerade
                    dir = direction[idx_new]['symbol_id']
                   # print(dir)
                else:   #gerade
                    idx_new = int(idx / 2)
                    dir = direction[idx_new]['symbol_id']

                result[val[0]] = {'dir': dir, 'force': force}

      #  print(json.dumps(result,ensure_ascii=False))
        return result

    def forcastWindByDay(self,stationId):

        result = {}

        url = self.getStationPrediction(stationId)
        response = self.getAPIcall(url)

        for list in response:
            wind = (list['wind']['data'])
            #variance = (list['variance_range'])
            timestamp = (list['min_date'])

            max = 0
            for idx, val in enumerate(wind):
                if max < wind[idx][1]:
                    max = wind[idx][1]

            result[timestamp] = {'max' :max}

       # print(json.dumps(result, ensure_ascii=False))

        return result

    def measuredWindSpeed(self,stationId):

        result = {}

        url = self.getMeasurement(stationId)
        response = self.getAPIcall(url)

        for list in response:
            wind = (list['wind']['data'])

            for idx, val in enumerate(wind):
                result[wind[idx][0]] = wind[idx][1]

        return result

    def currentWindSpeed(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
        response = self.getAPIcall(url)

        for list in response:
            result = list['wind']['data'][-1]

        return result