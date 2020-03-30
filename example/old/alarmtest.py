
import meteoswiss
import time
import datetime

class alarmTest(object):

    def __init__(self, plz):

        self._plz = plz
        print(plz)

    def xx(self):
        x = self._ms.getMeasurementV3('305300')
        for k,i in x.items():
            print(k)
      #  print(x['messwerte-niederschlag-10min'])
        return

    def rain(self):
        print(self._stationId)
        x = self._ms.rainLastYear('305300')
       # print(x)
        for k,i in x.items():
          #  timedate = datetime.fromtimestamp(k)
            dt3 = datetime.datetime.fromtimestamp(k / 1000)
         #   d =time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(k))
            value = i.get('rain',0)
            print(dt3,value)
        y = self._ms.rainLast3Days('305300')
        print('################################')
  #      print(y)
        for k,i in y.items():
          #  timedate = datetime.fromtimestamp(k)
            dt3 = datetime.datetime.fromtimestamp(k / 1000)
         #   d =time.strftime("%a, %d %b %Y %H9:%M:%S %Z", time.localtime(k))
            value = i.get('rain',0)
            print(dt3,value)

    def forcast(self):
        print(self._ms.sunforcastHour('305300'))

    def getStation(self):
        self._ms = meteoswiss.meteoswissApi()
        self._stationId = self._ms.getStationByAreaCode(self._plz)
        print(self._stationId)
        print(self._ms.getStationByAreaCode('3011'))

    def warning(self):
        self._ms.getWarning('305300')
        self._ms.getWarning('800100')

    def getMe(self):
        self._ms.getMeasurement()
        print(self._ms.getWarnRegion())
        print(self._ms.warningCurrent('800100'))
        print(self._ms.warningCurrent('305300'))
        print(self._ms.warningCurrent('301100'))

    def warningForcast(self):
        print(self._ms.warningForcast('800100'))

    def Sun(self):
        print('Sunrise:',self._ms.sunRiseForcast5Days('305300'))
        print('Sunset', self._ms.sunSetForcast5Days('305300'))

        print(self._ms.sunRiseForcast5Days('800100'))
        print(self._ms.sunSetForcast5Days('800100'))
if __name__ == "__main__":
    alarm = alarmTest('3053')
   # print(fc)

    alarm.getStation()
    alarm.xx()
    alarm.rain()
    alarm.forcast()

   # for k,i in alarm.xx().items():
    #    print(k)
 #   alarm.Sun()
 #   alarm.warningForcast()
 #   alarm.getMe()
 #   while(True):
  #      alarm.getMe()
   #     time.sleep(20)

