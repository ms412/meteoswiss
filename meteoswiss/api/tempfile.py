

import json

import logging

_classLogger = logging.getLogger(__name__)


#STATE = {"1":"sonnig","2":"ziemlich sonnig","3":"teilweise sonnig","4":"wechselnd bewölkt","5":"bedeckt","6":"Aufhellungen, einzelne Regenschauer","7":"Aufhellungen, einzelne Regen- oder Schneeschauer","8":"Aufhellungen, einzelne Schneeschauer","9":"bewölkt, einige Regenschauer","10":"bewölkt, einige Regen- oder Schneeschauer","11":"bewölkt, einige Schneeschauer","12":"Aufhellungen, leicht gewitterhaft","13":"Aufhellungen und gewitterhaft","14":"stark bewölkt, schwacher Regen","15":"stark bewölkt, schwacher Schnee oder Regen","16":"stark bewölkt, schwacher Schnee","17":"stark bewölkt, zeitweise Regen","18":"stark bewölkt, zeitweise Schnee oder Regen","19":"stark bewölkt, zeitweise Schnee","20":"stark bewölkt, anhaltender Regen","21":"stark bewölkt, anhaltender Regen oder Schnee","22":"stark bewölkt, anhaltender Schnee","23":"stark bewölkt, leicht gewitterhaft","24":"stark bewölkt, gewitterhaft","25":"stark bewölkt, stark gewitterhaft","26":"Hohe Bewölkung","27":"Hochnebel","28":"Nebel","29":"leicht bewölkt, einzelne Regenschauer","30":"leicht bewölkt, leichter Schneefall","31":"teilweise sonnig, einige Schnee- oder Regenschauer","32":"teilweise sonnig, einige Regenschauer","33":"bewölkt, häufige Regenschauer","34":"bewölkt, häufige Regenschauer","35":"bedeckt und trocken","101":"klar","102":"leicht bewölkt","103":"zum Teil bewölkt","104":"wechselnd bewölkt","105":"bedeckt","106":"Aufhellungen, einzelne Regenschauer","107":"Aufhellungen, einzelne Regen- oder Schneeschauer","108":"Aufhellungen, einzelne Schneeschauer","109":"bewölkt, einige Regenschauer","110":"bewölkt, einige Regen- oder Schneeschauer","111":"bewölkt, einige Schneeschauer","112":"Aufhellungen, leicht gewitterhaft","113":"Aufhellungen und gewitterhaft","114":"stark bewölkt, schwacher Regen","115":"stark bewölkt, schwacher Schnee oder Regen","116":"stark bewölkt, schwacher Schnee","117":"stark bewölkt, zeitweise Regen","118":"stark bewölkt, zeitweise Schnee oder Regen","119":"stark bewölkt, zeitweise Schnee","120":"stark bewölkt, anhaltender Regen","121":"stark bewölkt, anhaltender Regen oder Schnee","122":"stark bewölkt, anhaltender Schnee","123":"stark bewölkt, leicht gewitterhaft","124":"stark bewölkt, gewitterhaft","125":"stark bewölkt, stark gewitterhaft","126":"Hohe Bewölkung","127":"Hochnebel","128":"Nebel","129":"leicht bewölkt, einzelne Regenschauer","130":"leicht bewölkt, leichter Schneefall","131":"teilweise sonnig, einige Schnee- oder Regenschauer","132":"teilweise sonnig, einige Regenschauer","133":"bewölkt, häufige Regenschauer","134":"bewölkt, häufige Regenschauer","135":"bedeckt und trocken"}
STATE = {'1':'sonnig','2':'ziemlich sonnig','3':'teilweise sonnig','4':'wechselnd bewölkt','5':'bedeckt','6':'Aufhellungen, einzelne Regenschauer','7':'Aufhellungen, einzelne Regen- oder Schneeschauer','8':'Aufhellungen, einzelne Schneeschauer','9':'bewölkt, einige Regenschauer','10':'bewölkt, einige Regen- oder Schneeschauer','11':'bewölkt, einige Schneeschauer','12':'Aufhellungen, leicht gewitterhaft','13':'Aufhellungen und gewitterhaft','14':'stark bewölkt, schwacher Regen','15':'stark bewölkt, schwacher Schnee oder Regen','16':'stark bewölkt, schwacher Schnee','17':'stark bewölkt, zeitweise Regen','18':'stark bewölkt, zeitweise Schnee oder Regen','19':'stark bewölkt, zeitweise Schnee','20':'stark bewölkt, anhaltender Regen','21':'stark bewölkt, anhaltender Regen oder Schnee','22':'stark bewölkt, anhaltender Schnee','23':'stark bewölkt, leicht gewitterhaft','24':'stark bewölkt, gewitterhaft','25':'stark bewölkt, stark gewitterhaft','26':'Hohe Bewölkung','27':'Hochnebel','28':'Nebel','29':'leicht bewölkt, einzelne Regenschauer','30':'leicht bewölkt, leichter Schneefall','31':'teilweise sonnig, einige Schnee- oder Regenschauer','32':'teilweise sonnig, einige Regenschauer','33':'bewölkt, häufige Regenschauer','34':'bewölkt, häufige Regenschauer','35':'bedeckt und trocken','101':'klar','102':'leicht bewölkt','103':'zum Teil bewölkt','104':'wechselnd bewölkt','105':'bedeckt','106':'Aufhellungen, einzelne Regenschauer','107':'Aufhellungen, einzelne Regen- oder Schneeschauer','108':'Aufhellungen, einzelne Schneeschauer','109':'bewölkt, einige Regenschauer','110':'bewölkt, einige Regen- oder Schneeschauer','111':'bewölkt, einige Schneeschauer','112':'Aufhellungen, leicht gewitterhaft','113':'Aufhellungen und gewitterhaft','114':'stark bewölkt, schwacher Regen','115':'stark bewölkt, schwacher Schnee oder Regen','116':'stark bewölkt, schwacher Schnee','117':'stark bewölkt, zeitweise Regen','118':'stark bewölkt, zeitweise Schnee oder Regen','119':'stark bewölkt, zeitweise Schnee','120':'stark bewölkt, anhaltender Regen','121':'stark bewölkt, anhaltender Regen oder Schnee','122':'stark bewölkt, anhaltender Schnee','123':'stark bewölkt, leicht gewitterhaft','124':'stark bewölkt, gewitterhaft','125':'stark bewölkt, stark gewitterhaft','126':'Hohe Bewölkung','127':'Hochnebel','128':'Nebel','129':'leicht bewölkt, einzelne Regenschauer','130':'leicht bewölkt, leichter Schneefall','131':'teilweise sonnig, einige Schnee- oder Regenschauer','132':'teilweise sonnig, einige Regenschauer','133':'bewölkt, häufige Regenschauer','134':'bewölkt, häufige Regenschauer','135':'bedeckt und trocken'}

class  tempfile(object):

    def __init__(self):
        self._filepath

    def filename(self,filepath):
        self._fielpath = filepath

    def read(self,content):
        with open(self._fielpath) as json_file:
            content = json.load(json_file)

    def write(self):
        with open(self._fielpath, 'w') as outfile:
            json.dump(content, outfile)

        return content


