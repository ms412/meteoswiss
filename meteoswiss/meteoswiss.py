
from meteoswiss.api.location import location
from meteoswiss.api.weather import weather
from meteoswiss.api.rain import rain
from meteoswiss.api.temperature import temperature
from meteoswiss.api.sunshine import sunshine
from meteoswiss.api.wind import wind
from meteoswiss.api.measurement import measurement

class meteoswissApi(location, measurement,rain,temperature,sunshine,wind):

    pass
