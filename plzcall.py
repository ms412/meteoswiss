
import requests
import json

import logging

_LOGGER = logging.getLogger(__name__)


#STATE = {"1":"sonnig","2":"ziemlich sonnig","3":"teilweise sonnig","4":"wechselnd bewölkt","5":"bedeckt","6":"Aufhellungen, einzelne Regenschauer","7":"Aufhellungen, einzelne Regen- oder Schneeschauer","8":"Aufhellungen, einzelne Schneeschauer","9":"bewölkt, einige Regenschauer","10":"bewölkt, einige Regen- oder Schneeschauer","11":"bewölkt, einige Schneeschauer","12":"Aufhellungen, leicht gewitterhaft","13":"Aufhellungen und gewitterhaft","14":"stark bewölkt, schwacher Regen","15":"stark bewölkt, schwacher Schnee oder Regen","16":"stark bewölkt, schwacher Schnee","17":"stark bewölkt, zeitweise Regen","18":"stark bewölkt, zeitweise Schnee oder Regen","19":"stark bewölkt, zeitweise Schnee","20":"stark bewölkt, anhaltender Regen","21":"stark bewölkt, anhaltender Regen oder Schnee","22":"stark bewölkt, anhaltender Schnee","23":"stark bewölkt, leicht gewitterhaft","24":"stark bewölkt, gewitterhaft","25":"stark bewölkt, stark gewitterhaft","26":"Hohe Bewölkung","27":"Hochnebel","28":"Nebel","29":"leicht bewölkt, einzelne Regenschauer","30":"leicht bewölkt, leichter Schneefall","31":"teilweise sonnig, einige Schnee- oder Regenschauer","32":"teilweise sonnig, einige Regenschauer","33":"bewölkt, häufige Regenschauer","34":"bewölkt, häufige Regenschauer","35":"bedeckt und trocken","101":"klar","102":"leicht bewölkt","103":"zum Teil bewölkt","104":"wechselnd bewölkt","105":"bedeckt","106":"Aufhellungen, einzelne Regenschauer","107":"Aufhellungen, einzelne Regen- oder Schneeschauer","108":"Aufhellungen, einzelne Schneeschauer","109":"bewölkt, einige Regenschauer","110":"bewölkt, einige Regen- oder Schneeschauer","111":"bewölkt, einige Schneeschauer","112":"Aufhellungen, leicht gewitterhaft","113":"Aufhellungen und gewitterhaft","114":"stark bewölkt, schwacher Regen","115":"stark bewölkt, schwacher Schnee oder Regen","116":"stark bewölkt, schwacher Schnee","117":"stark bewölkt, zeitweise Regen","118":"stark bewölkt, zeitweise Schnee oder Regen","119":"stark bewölkt, zeitweise Schnee","120":"stark bewölkt, anhaltender Regen","121":"stark bewölkt, anhaltender Regen oder Schnee","122":"stark bewölkt, anhaltender Schnee","123":"stark bewölkt, leicht gewitterhaft","124":"stark bewölkt, gewitterhaft","125":"stark bewölkt, stark gewitterhaft","126":"Hohe Bewölkung","127":"Hochnebel","128":"Nebel","129":"leicht bewölkt, einzelne Regenschauer","130":"leicht bewölkt, leichter Schneefall","131":"teilweise sonnig, einige Schnee- oder Regenschauer","132":"teilweise sonnig, einige Regenschauer","133":"bewölkt, häufige Regenschauer","134":"bewölkt, häufige Regenschauer","135":"bedeckt und trocken"}
STATE = {'1':'sonnig','2':'ziemlich sonnig','3':'teilweise sonnig','4':'wechselnd bewölkt','5':'bedeckt','6':'Aufhellungen, einzelne Regenschauer','7':'Aufhellungen, einzelne Regen- oder Schneeschauer','8':'Aufhellungen, einzelne Schneeschauer','9':'bewölkt, einige Regenschauer','10':'bewölkt, einige Regen- oder Schneeschauer','11':'bewölkt, einige Schneeschauer','12':'Aufhellungen, leicht gewitterhaft','13':'Aufhellungen und gewitterhaft','14':'stark bewölkt, schwacher Regen','15':'stark bewölkt, schwacher Schnee oder Regen','16':'stark bewölkt, schwacher Schnee','17':'stark bewölkt, zeitweise Regen','18':'stark bewölkt, zeitweise Schnee oder Regen','19':'stark bewölkt, zeitweise Schnee','20':'stark bewölkt, anhaltender Regen','21':'stark bewölkt, anhaltender Regen oder Schnee','22':'stark bewölkt, anhaltender Schnee','23':'stark bewölkt, leicht gewitterhaft','24':'stark bewölkt, gewitterhaft','25':'stark bewölkt, stark gewitterhaft','26':'Hohe Bewölkung','27':'Hochnebel','28':'Nebel','29':'leicht bewölkt, einzelne Regenschauer','30':'leicht bewölkt, leichter Schneefall','31':'teilweise sonnig, einige Schnee- oder Regenschauer','32':'teilweise sonnig, einige Regenschauer','33':'bewölkt, häufige Regenschauer','34':'bewölkt, häufige Regenschauer','35':'bedeckt und trocken','101':'klar','102':'leicht bewölkt','103':'zum Teil bewölkt','104':'wechselnd bewölkt','105':'bedeckt','106':'Aufhellungen, einzelne Regenschauer','107':'Aufhellungen, einzelne Regen- oder Schneeschauer','108':'Aufhellungen, einzelne Schneeschauer','109':'bewölkt, einige Regenschauer','110':'bewölkt, einige Regen- oder Schneeschauer','111':'bewölkt, einige Schneeschauer','112':'Aufhellungen, leicht gewitterhaft','113':'Aufhellungen und gewitterhaft','114':'stark bewölkt, schwacher Regen','115':'stark bewölkt, schwacher Schnee oder Regen','116':'stark bewölkt, schwacher Schnee','117':'stark bewölkt, zeitweise Regen','118':'stark bewölkt, zeitweise Schnee oder Regen','119':'stark bewölkt, zeitweise Schnee','120':'stark bewölkt, anhaltender Regen','121':'stark bewölkt, anhaltender Regen oder Schnee','122':'stark bewölkt, anhaltender Schnee','123':'stark bewölkt, leicht gewitterhaft','124':'stark bewölkt, gewitterhaft','125':'stark bewölkt, stark gewitterhaft','126':'Hohe Bewölkung','127':'Hochnebel','128':'Nebel','129':'leicht bewölkt, einzelne Regenschauer','130':'leicht bewölkt, leichter Schneefall','131':'teilweise sonnig, einige Schnee- oder Regenschauer','132':'teilweise sonnig, einige Regenschauer','133':'bewölkt, häufige Regenschauer','134':'bewölkt, häufige Regenschauer','135':'bedeckt und trocken'}

class  viConnect(object):

    def call(self,url):

        response = requests.get(url,timeout=10)
        if response.ok:
            return response.json()
        else:
            return False



    def plz(self,plz):
        result = []
        _plz = str(plz)[:2]
        print(_plz)
        call = 'https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/%s.json'%_plz
        print(call)

        response = self.call(call)
        #print(response.content)
        for x in response:
            z = x.split(';')
        #    print(x.split(';'), len(x.split(';')))
         #   print(type(z[3]),z[3])
            if str(plz) in z[3]:
          #      print(z)
                result.append(z[0])

        return result

    def ort(self,ort):
        result = []
        _plz = ort.lower()[:2]
        print(_plz)
        call = 'https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/%s.json'%_plz
        print(call)
        response = requests.get(call)
        print(response.encoding)
        print(response.status_code)
        print(response.headers)
        print(response.text)
        print(response.json)

        print(type(response.json))
        for x in  response.json():
            z = x.split(';')
            print (x.split(';'), len(x.split(';')))
            if len(z) == 6:
                if ort.lower() in z[5].lower():
                    print(z[5])
                    result.append(z[0])
             #   print(z[5])
        return result

    def getData(self,stationId):
        _stationId=str(stationId[0])
        url = 'https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz=%s'%_stationId
        response = requests.get(url)
        print(response.status_code)
       # print(response.text)
        _data = response.json()['forecast'][0]['precipitation']
        for n, val in enumerate(response.json()['forecast']):
         #   print(n)
            _data = response.json()['forecast'][n]['precipitation']
            print(n, _data)

        _data = response.json()['forecast'][0]['precipitation']
        print(type(STATE))
       # _state = json.loads(STATE)
        for n, val in enumerate(response.json()['forecast']):
           # print(val)
            _icon = response.json()['forecast'][n]['iconDay']
            _max = response.json()['forecast'][n]['temperatureMin']
            _min = response.json()['forecast'][n]['temperatureMax']
            print(n, _min, _max, STATE.get(str(_icon),'unknown'))

if __name__ == "__main__":
    vi = viConnect()
    stationId = (vi.plz(3052))
    print('Station ID:', stationId)
    vi.getData(stationId)
 #   print(vi.ort('Bern'))
#    print(vi)
    print(STATE.get(str(1)))

