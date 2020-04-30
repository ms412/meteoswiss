
# Version 0.8
# last change 30.4.2020

from meteoswiss.api.location import location
from meteoswiss.api.rain import rain
from meteoswiss.api.temperature import temperature
from meteoswiss.api.sunshine import sunshine
from meteoswiss.api.wind import wind
from meteoswiss.api.pressure import pressure
from meteoswiss.api.humidity import humidity
from meteoswiss.api.measurement import measurement
from meteoswiss.api.warning import warning

class meteoswiss(location,
                    measurement,
                    warning,
                    rain,
                    pressure,
                    humidity,
                    temperature,
                    sunshine,
                    wind):

    pass
