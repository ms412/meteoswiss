
import pandas as pd
import meteoswiss
import datetime



class forcastDemo(object):

    def __init__(self,plz):
        self._ms = meteoswiss.meteoswissApi()
        self._stationId = self._ms.getStationByAreaCode(plz)[0]

    def dataframe(self,data):
        df = pd.DataFrame.from_dict(data, orient="index")
        df['datetime'] = pd.to_datetime(df.index, unit='ms')
        df = df.set_index('datetime')
        df.index = pd.DatetimeIndex(df.index)
        return df

    def rain(self):
        print('### Rain ###')
        week = self._ms.rainforcastWeek(self._stationId)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def sunshine(self):
        print('### Sunshine ###')
        week = self._ms.sunForcastWeek(self._stationId)
       # self._print(week)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def temperature(self):
        print('### Temperature ###')
        week = self._ms.temperatureForcastWeek(self._stationId)
      #  self._print(week)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def wind(self):
        print('### Wind ###')
        week = self._ms.windForcastWeek(self._stationId)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def measurementLast(self):
        week = self._ms.windLast3Days(self._stationId)
    #    print(week)
        df = self.dataframe(week)
        print(df.resample('D').sum())

        week = self._ms.windLastYear(self._stationId)
   #     print(week)
        df = self.dataframe(week)
        print(df.resample('M').sum())

    def warrning(self):
        warning = self._ms.warningCurrent(self._stationId)
        print('Current', warning)
        warning = self._ms.warningForcast(self._stationId)
        print('Forcast', warning)













if __name__ == "__main__":

    forcast = forcastDemo(3800)
    forcast.rain()
    forcast.sunshine()
    forcast.temperature()
    forcast.wind()
    forcast.measurementLast()
    forcast.warrning()
    #forcast.panda()