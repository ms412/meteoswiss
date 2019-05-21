
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class pressure(object):

     def pressureLast3days(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        qfe = response['messwerte-luftdruck-qfe-10min']['days'][0]['data']
        qnh = response['messwerte-luftdruck-qnh-10min']['days'][0]['data']
        qff = response['messwerte-luftdruck-qff-10min']['days'][0]['data']
        hpaA = response['messwerte-luftdruck-850hpa-flaeche-10min']['days'][0]['data']
        hpaB = response['messwerte-luftdruck-700hpa-flaeche-10min']['days'][0]['data']
      #  windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][1]['data']
       # windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][2]
       # windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

        for idx, val in enumerate(qfe):
          #  print(idx, val[0], val[1], qnh[idx][1], qff[idx][1], hpaA[idx][1], hpaB[idx][1])
            x = {'qfe':qfe[idx][1],'qnh':qnh[idx][1],'qff':qff[idx][1],'850hpa':hpaA[idx][1],'700hpa':hpaB[idx][1]}
            result[val[0]] = x

      #  print(json.dumps(result, ensure_ascii=False))
        return result

     def pressureLastYear(self,stationId):

        result = {}
        response = self.getMeasurementV3(stationId)
       # print(response)

        qfe = response['messwerte-luftdruck-qfe-10min']['year'][0]['data']
        qnh = response['messwerte-luftdruck-qnh-10min']['year'][0]['data']
        qff = response['messwerte-luftdruck-qff-10min']['year'][0]['data']
        hpaA = response['messwerte-luftdruck-850hpa-flaeche-10min']['year'][0]['data']
        hpaB = response['messwerte-luftdruck-700hpa-flaeche-10min']['year'][0]['data']
      #  windSpeed = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][1]['data']
       # windDir = response['messwerte-windgeschwindigkeit-kmh-10min']['days'][2]
       # windSpeedPeak = response['messwerte-wind-boeenspitze-kmh-10min']

        for idx, val in enumerate(qfe):
          #  print(idx, val[0], val[1], qnh[idx][1], qff[idx][1], hpaA[idx][1], hpaB[idx][1])
            x = {'qfe':qfe[idx][1],'qnh':qnh[idx][1],'qff':qff[idx][1],'850hpa':hpaA[idx][1],'700hpa':hpaB[idx][1]}
            result[val[0]] = x

       # print(json.dumps(result, ensure_ascii=False))
        return result


