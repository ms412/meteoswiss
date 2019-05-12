
import sys
import meteoswiss
from configobj import ConfigObj
from library.loghandler import loghandler

class forcastRain(object):
    def __init__(self,configfile):

        self._configfile = configfile
        self._log = None

    def readConfig(self):
        print('READCONFIG',self._configfile)
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
        self._log.critical('TEST')
        return True

    def querry(self):
        ms = meteoswiss.meteoswissApi()
        ms.getStationByAreaCode(3000)
        ms.getStationByName('Bern')
        ms.getStationDetails('305200')

    def test(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByName('Bern')
        print(str(id[0]))
        path = ms.getStationPrediction(str(id[0]))
        print(path)
        print(ms.forcastRainByHour(str(id[0])))
        print( ms.forcastRainByDay(str(id[0])))

    def measurement(self):
        ms = meteoswiss.meteoswissApi()
        id = ms.getStationByName('Bern')
        print(str(id[0]))
        print(ms.getStationMeasurement(str(id[0])))

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

    def getSunrise(self):
        ms = meteoswiss.meteoswissApi()
        ms.getSunset(305200)
        ms.getSunset(120100)
        ms.getSunrise(305200)
        ms.getSunrise(120100)


    def run(self):
        self.readConfig()
        self.startLogger()
        self.querry()
     #   self.test()
       # self.measurement()
        #self.temperature()
       # self.sunshine()
        self.getSunrise()
       # self.connect()
        #self.calls()


if __name__ == "__main__":
    fc = forcastRain('./forcastRain.cfg')
    print(fc)
    fc.run()
