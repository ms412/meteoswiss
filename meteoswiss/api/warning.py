
import re
import json
import requests
from lxml import html, etree
import logging
import meteoswiss.api.base as base

_classLogger = logging.getLogger(__name__)



class warning(base.apiClient):

    def getWarningOverview(self,stationId='800100'):

        results= []

        warningType = {
            1:'Thunderstorm', 2:'Rain',11:'Flood',10:'ForestFire'
        }

        #https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz= 300500
        response = self.getAPIcall('https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz={}'.format(stationId))

     #   print(json.dumps(response, ensure_ascii=False))

        for item in response['warningsOverview']:
          #  print(item,item.get('warnType',99))
            results.append({'warnType':warningType.get(item['warnType'],'Unknown'),'warnLevel':item.get('warnLevel')})

        return results

    def getWarning(self,stationId='800100'):

        results= []

        warningType = {
            1:'Thunderstorm', 2:'Rain',11:'Flood',10:'ForestFire'
        }

      #  self._appUrl = 'https://app-prod-ws.meteoswiss-app.ch'
        #https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz= 300500
        response = self.getAPIcall('https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz=' + str(stationId))

       # print(json.dumps(response, ensure_ascii=False))

        for item in response['warnings']:
         #   print(item,item.get('warnType',99))
            results.append({'warnType':warningType.get(item['warnType'],'Unknown'),
                            'warnLevel':item.get('warnLevel'),
                            'validFrom':item.get('validFrom'),
                            'validTo' :item.get('validTo'),
                            'text' :item.get('text')
                            })

        return results