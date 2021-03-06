
import sys
import meteoswiss
from configobj import ConfigObj
from library.loghandler import loghandler

class forcastRain(object):
    def __init__(self,configfile):

        self._configfile = configfile
        self._log = None

    def readConfig(self):
       # print('READCONFIG',self._configfile)
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        return True

    def startLogger(self):
        self._log = loghandler()
        self._log.handle(self._cfg_log.get('LOGMODE'), self._cfg_log)
        self._log.level(self._cfg_log.get('LOGLEVEL', 'DEBUG'))
       # self._log.critical('TEST')
        return True

    def createObj(self):
        self._ms = meteoswiss.meteoswissApi()
        self._station1 = self._ms.getStationByVillage('Zermatt')[0]
        self._station2 = self._ms.getStationByAreaCode(3053)[0]
        print('Station 1:',self._station1)
        print('Station 2:',self._station2)


    def test(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByVillage('Bern')
        print(str(id[0]))
        path = ms.getPrediction(str(id[0]))
        print(path)
        print(ms.forcastRainByHour(str(id[0])))
        print( ms.forcastRainByDay(str(id[0])))

    def measurement(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByVillage('Bern')
        print(str(id[0]))
        print(ms.getMeasurementByStationCode(str(id[0])))

    def temperature(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByAreaCode('3052')
        print(str(id))
        print(ms.forcastTemperatureByDay(str(id[0])))
       # print(ms.forcastTemperatureByHour(str(id[0])))

    def sunshine(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByAreaCode('3052')
        print(str(id))
        print(ms.forcastSunshineByDay(str(id[0])))
        print(ms.forcastSunshineByHour(str(id[0])))

    def Sunshine(self):
        print('Sunset Station 1')
        print(self._ms.getSunset(self._station1))
        print('Sunset Station 2')
        print(self._ms.getSunset(self._station2))
        print('Sunrise Station 1')
        print(self._ms.getSunrise(self._station1))
        print('Sunrise Station 2')
        print(self._ms.getSunrise(self._station2))
        print('Sunshine Forcast by Day Station 1')
        print(self._ms.forcastSunshineByDay(self._station1))
        print('Current Sunshine Station 1')
        print(self._ms.currentSunshine(self._station1))
        print('Measured Sunshine Station 1')
        print(self._ms.historicalSunshine(self._station1))
        print(self._ms.sunshineLast3Days(self._station1))
        print(self._ms.sunshineLastYear(self._station1))

    def Wind(self):
        print('Forcast wind speed by Hour and direction',self._ms.forcastWindByHour(self._station1))
        print('Forcast max wind speed by day',self._ms.forcastWindByDay(self._station1))
        print('Measured wind speed',self._ms.measuredWindSpeed(self._station1))
        print('Current Wind Speed',self._ms.currentWindSpeed(self._station1))

    def Rain(self):
        print('Forcast Rain by Hour', self._ms.forcastRainByDay(self._station1))
        print('Measured Rain last Days', self._ms.rainLast3Days(self._station1))
        print ('Measured Rain last Year', self._ms.rainLastYear(self._station1))

    def Temperature(self):
       # self._ms.temperatureLast3days(self._station2)
        self._ms.temperatureLastYear(self._station1)

    def Pressure(self):
        print('Pressur during last 3 days',self._ms.pressureLast3Days(self._station2))
        print('Pressur during last year',self._ms.pressureLastYear(self._station2))
        print('Pressur current',self._ms.pressureCurrent(self._station2))

    def Humidity(self):
        print('Current humidity',self._ms.humiditCurrent(self._station1))
        print('Humidity last 3 days', self._ms.humidityLast3Days(self._station2))
        print('Humidity last year', self._ms.humidityLastYear(self._station2))

    def getMeasurements(self):
      #  self._ms.getMeasurementV3(self._station1)
        print(self._ms.windLast3days(self._station1))
        print(self._ms.windLastYear(self._station1))
        print(self._ms.getWarning(self._station1))
        print(self._ms.getWarning(self._station2))

    def getMeasurement(self):
        ms = meteoswiss.meteoswissApi()
        print(ms.getMeasurement())


    def run(self):
        self.readConfig()
        self.startLogger()
        self.createObj()
     #   self.test()
       # self.measurement()
        #self.temperature()
      #  self.sunshine()
        self.Rain()
        #self.Temperature()
        self.Pressure()
        self.Humidity()

     #   self.Sunshine()
       # self.getMeasurements()
     #   self.Wind()
       # self.getMeasurement()
       # self.connect()
        #self.calls()


if __name__ == "__main__":
    fc = forcastRain('./forcastRain.cfg')
   # print(fc)
    fc.run()
