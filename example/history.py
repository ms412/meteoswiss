

import pandas as pd
import meteoswiss
import datetime



class historyDemo(object):

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
        week = self._ms.rainHistory1y(self._stationId)
        df = self.dataframe(week)
        print(df.resample('M').sum())

    def sunshine(self):
        print('### Sunshine ###')
        week = self._ms.sunHistory1y(self._stationId)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def temperature(self):
        print('### Temperature ###')
        week = self._ms.temperatureHistory1y(self._stationId)
        df = self.dataframe(week)
        print(df.resample('D').sum())

    def wind(self):
        print('### Wind ###')
        week = self._ms.windHistory3d(self._stationId)
        df = self.dataframe(week)
        print(df.resample('h').sum())

        week = self._ms.windHistory1y(self._stationId)
        df = self.dataframe(week)
        print(df.resample('M').sum())


if __name__ == "__main__":

    history = historyDemo(3800)
    history.rain()
    history.sunshine()
    history.temperature()
    history.wind()
    #forcast.measurementLast()
    #forcast.warrning()
    #forcast.panda()