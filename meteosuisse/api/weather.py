
import requests


class Weather(object):

    def __init__(self):
        print('Test')

    def getStation(self,plz):
        result = requests.get('https://www.meteoswiss.admin.ch/etc/designs/meteoswiss/ajax/search/3.json')