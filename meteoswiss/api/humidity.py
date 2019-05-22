
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class humidity(object):

     def humiditCurrent(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)

        humidity = response['messwerte-luftfeuchtigkeit-10min']['days'][0]['data']

        result = {'humidity':humidity[0][1],'date':humidity[0][0]}

        return result

     def humidityLast3Days(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)

        humidity = response['messwerte-luftfeuchtigkeit-10min']['days'][0]['data']

        for idx, val in enumerate(humidity):
            print(idx,val)
            x = {'humidity':val[1]}
            result[val[0]] = x

      #  print(json.dumps(result, ensure_ascii=False))
        return result

     def humidityLastYear(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)

        humidity = response['messwerte-luftfeuchtigkeit-10min']['year'][0]['data']

        for idx, val in enumerate(humidity):
            x = {'humidity': val[1]}
            result[val[0]] = x

       # print(json.dumps(result, ensure_ascii=False))
        return result


