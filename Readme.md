
API to query data from https://www.meteoswiss.admin.ch

This library doesn't use documented interfaces. This library use calls by web scraping or calls used by the Android app of Swiss Meteo. 
Those calls can be subject of change at any time!


**Humidity:**

humidityCurrent(stationId)

humidityHistroy1y(stationId)

humidityHistory3d(stationId)

**Pressure:**
pressureCurrent(staionId)

pressureHistory3d(stationId)

pressureHistory1y(stationId)

**Rainfall:**

rainCurrent(stationId)

rainforcastToday(stationId)

rainforcastWeek(stationId)

rainHistory1y(stationId)

rainHistory3d(stationId)

**Sunshine:**

sunCurrent(stationId)

sunForcastToday(stationId)

sunForcastWeek(stationId)

sunHistory1y(stationId)

sunHistory3d(stationId)

sunRiseForcast(stationId)

sunSetForcast(stationId)

**Temperature:**

temperatureCurrent(stationId)

temperatureForcastWeek(stationId)

termperatureHistory1y(stationId)

termperatureHistory3d(stationId)

**Wind:**

windCurrent(stationId)

windForcastWeek(stationId)

windHistory1y(stationId)

windHistory3d(stationId)

**Warning:**

warningCurrent(stationId)

warningForcast(stationId)

**Example:**

``
ms = meteoswiss.meteoswiss()
stationId = ms.getStationByAreaCode(3011)[0]
ms.temperatureCurrent(self._stationId)[1]``





