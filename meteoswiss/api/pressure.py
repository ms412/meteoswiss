
import json
import logging
import meteoswiss.api.base
import meteoswiss.api.location

_classLogger = logging.getLogger(__name__)

class pressure(object):

     def pressureCurrent(self,stationId):

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

        #for idx, val in enumerate(qfe):
          #  print(idx, val[0], val[1], qnh[idx][1], qff[idx][1], hpaA[idx][1], hpaB[idx][1])
        result = {'qfe':qfe[0][1],'qnh':qnh[0][1],'qff':qff[0][1],'850hpa':hpaA[0][1],'700hpa':hpaB[0][1]}
         #   result[val[0]] = x

      #  print(json.dumps(result, ensure_ascii=False))
        return result

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


#QNH oder QFF – Wo liegt der Unterschied?
#Als QNH (Question Normal Height) bezeichnet man den auf Meereshöhe reduzierten
#Luftdruck an einer Messstation. Die Umrechnung des Luftdrucks von Stations- auf
#Meereshöhe basiert auf einem standardisierten vertikalen Temperaturverlauf, wobei
#die Ausgangstemperatur der in der Aviatik gebräuchlichen Standardatmosphäre [ISA
#= International Standard Atmosphäre] entnommen wird.
#Als QFF bezeichnet man den auf Meereshöhe reduzierten Luftdruck an einer Messstation. Die Umrechnung des Luftdrucks von Stations- auf Meereshöhe basiert auf
#einem standardisierten vertikalen Temperaturverlauf, wobei die Ausgangstemperatur
#aus einer aktuellen Messung stammt.
#Im Gegensatz zum QFF wird beim QNH als Temperaturwert nicht die aktuelle Messung, sondern die zur Ortshöhe korrespondierende ISA Temperatur verwendet. Das
#QFF liegt im Allgemeinen näher bei der Realität als das QNH. Da die druckbasierten
#Höhenmesser gemäss der ISA genormt sind, wird in der Aviatik aber vorwiegend das
#QNH verwendet.