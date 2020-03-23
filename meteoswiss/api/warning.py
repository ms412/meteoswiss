
import re
import json
import requests
from lxml import html, etree
from datetime import datetime
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)


class warning(base.apiClient):

    def  warningCurrent(self,stationId='800100'):
        _result = {}

        _region = self.getWarnRegion(stationId)

        _now = datetime.now()
        _today = _now.strftime("%Y%m%d")
        _today24h = _today +"_24h"
        _rawData = self.getWarning(stationId)['days'][_today24h]['hazards']

        _result[_today] = self._warningFilterHelper(_rawData,_region)

        return _result

    def warningForcast(self, stationId='800100'):
        _result = {}

        _region = self.getWarnRegion(stationId)

        _now = datetime.now()
        _dateString = _now.strftime("%Y%m%d")
        _rawData = self.getWarning(stationId)['days']

        for key,item in _rawData.items():
            if len(key) > 8:
                _date = _dateString
               # _result[_dateString] = {}
            else:
                _date = key
              #  _result[_da] = {}

            _result[_date] = self._warningFilterHelper(item['hazards'],_region)

        return _result

    def _warningFilterHelper(self, data, region):
        _result = {}

        for key,item in data.items():
            if item is not None:
                _result[key] = {}
                for value in item:
                    if set(region).intersection(value['areas']):
                        _result[key]['LEVEL'] = value['warnlevel']
                        _result[key]['TYPE'] = value['warn_type']
                        _result[key]['ONSET'] = value['onset']
                        _result[key]['EXPIRE'] = value['expires']

        return _result
