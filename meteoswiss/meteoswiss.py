
from meteoswiss.api.location import location
from meteoswiss.api.rain import rain
from meteoswiss.api.temperature import temperature
from meteoswiss.api.sunshine import sunshine
from meteoswiss.api.wind import wind
from meteoswiss.api.pressure import pressure
from meteoswiss.api.measurement import measurement
from meteoswiss.api.warning import warning

class meteoswissApi(location,
                    measurement,
                    warning,
                    rain,
                    pressure,
                    temperature,
                    sunshine,
                    wind):

    pass
