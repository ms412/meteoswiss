
import sys
import time
import datetime
import meteoswiss

class Weather2mqtt(object):

    def __init__(self, plz):

        self._plz = plz

    def getStation(self):
        self._ms = meteoswiss.meteoswissApi()
        self._stationId = self._ms.getStationByAreaCode(self._plz)[0]

    def getTemperature(self):
        date, value = self._ms.currentTemperature(self._stationId)
        print(datetime.datetime.fromtimestamp(float(date)/1000).strftime('%Y-%m-%d %H:%M:%S'),value)
        return value

    def getRainfall(self):
        return self._ms.currentRainfall(self._stationId)[1]

    def getPressure(self):
        return self._ms.currentPressure(self._stationId)['qfe']

    def getSunshine(self):
        return self._ms.currentSunshine(self._stationId)[1]

    def getWindspeed(self):
        return self._ms.currentWindSpeed(self._stationId)[1]

    def getHumidity(self):
        date, value = self._ms.currentHumidity(self._stationId)
        print(date,time.time(),value)
        print(datetime.datetime.fromtimestamp(float(date)/1000).strftime('%Y-%m-%d %H:%M:%S'))
        return value

    def collectMeasurements(self):
        result = {"MeteoSwiss-Temperature" : self.getTemperature(),
                  "MeteoSwiss-Rainfall" : self.getRainfall(),
                  "MeteoSwiss-Pressure": self.getPressure(),
                  "MeteoSwiss-Sunshine" : self.getSunshine(),
                  "MeteoSwiss-Windspeed" : self.getWindspeed(),
                  "MeteoSwiss-Humidity" : self.getHumidity()}
        print('Result',result)


    def run(self):
        self.getStation()
        self.collectMeasurements()




if __name__ == "__main__":
    fc = Weather2mqtt(3053)
   # print(fc)
    fc.run()
