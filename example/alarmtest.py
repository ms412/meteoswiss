
import meteoswiss
import time

class alarmTest(object):

    def __init__(self, plz):

        self._plz = plz
        print(plz)

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
    alarm.Sun()
    alarm.warningForcast()
    alarm.getMe()
    while(True):
        alarm.getMe()
        time.sleep(20)

