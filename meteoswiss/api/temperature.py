
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class temperature(object):

    def temperaturForcastByHour(self,stationId):

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

    def temperaturForcastByDay(self,stationId):

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

    def temperatureCurrent(self,stationId):

        result = ''

        url = self.getMeasurement(stationId)
        print('xx',url)
        response = self.getAPIcall(url)

        for list in response:
            result = list['temperature'][-1]

        return result

    def temperatureLast3Days(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        avr = response['messwerte-lufttemperatur-10min']['days'][0]['data']
        min = response['messwerte-lufttemperatur-10min']['days'][1]['data']
        max = response['messwerte-lufttemperatur-10min']['days'][2]['data']
      #  windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][1]['data']
       # windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][2]
       # windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

        for idx, val in enumerate(avr):
            print(idx, val[0], val[1], avr[idx][1], min[idx][1], max[idx][1])
            x = {'avr':avr[idx][1],'min':min[idx][1],'max':max[idx][1]}
            result[val[0]] = x

        print(json.dumps(result, ensure_ascii=False))
        return result

    def temperatureLastYear(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        avr = response['messwerte-lufttemperatur-10min']['year'][0]['data']
      #  min = response['messwerte-lufttemperatur-10min']['year'][1]['data']
       # max = response['messwerte-lufttemperatur-10min']['year'][2]['data']
      #  windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][1]['data']
       # windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][2]
       # windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

        for idx, val in enumerate(avr):
            print(idx, val[0], val[1])    #, avr[idx][1], min[idx][1], max[idx][1])
            x = {'avr':avr[idx][1]} #,'min':min[idx][1],'max':max[idx][1]}
            result[val[0]] = x

        print(json.dumps(result, ensure_ascii=False))
        return result