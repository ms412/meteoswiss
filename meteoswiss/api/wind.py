
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class wind(object):

    def windForcastByHour(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
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

    def windForcastByDay(self,stationId):

        result = {}

        url = self.getPrediction(stationId)
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

    def windCurrent(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
        response = self.getAPIcall(url)

        for list in response:
            result = list['wind']['data'][-1]

        return result

    def windLast3Days(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        windSpeedGusts = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][0]
        windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][1]['data']
        windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][2]
        windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

        for idx, val in enumerate(windSpeed):
            print(idx, val[0], val[1], windSpeedGusts['data'][idx][1], windDir['data'][idx][1])
            x = {'wind':val[1],'gusts':windSpeedGusts['data'][idx][1],'dir':windDir['data'][idx][1]}
            result[val[0]] = x

       # print(json.dumps(result, ensure_ascii=False))
        return result

    def windLastYear(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
        # print(response)

        windSpeedGusts = response['messwerte-windgeschwindigkeit-kmh-10min']['year'][0]
        windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['year'][1]['data']
       # windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['year'][2]
        windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

    #    print(json.dumps(windSpeed, ensure_ascii=False))

        for idx, val in enumerate(windSpeed):
            #print(idx,windDir['data'][idx])
          #  print(idx, val[0], val[1], windSpeedGusts['data'][idx][1]) #, windDir['data'][idx][1])
            x = {'wind': val[1], 'gusts': windSpeedGusts['data'][idx][1]} #, 'dir': windDir['data'][idx][1]}
            result[val[0]] = x

         #print(result)
        #return json.dumps(result, ensure_ascii=False)
        return result
