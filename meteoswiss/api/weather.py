
import requests
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class weather(base.apiClient):

    def getStation(self,plz):

        _classLogger.debug('getStation')
        result = self.getAPIcall('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/3.json')