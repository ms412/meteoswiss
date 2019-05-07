
__app__ = "loghandler"
__VERSION__ = "1.0"
__DATE__ = "14.02.2018"
__author__ = "Markus Schiesser"
__contact__ = "Markus.Schiesser@swisscom.com"


import logging
import logging.handlers
import socket


class loghandler(object):
   # __metaclass__ = Singleton

    def __init__(self,name = None):  

        self._loghandle = ''

        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)

    def level(self,level):
        if level in 'INFO':
            self._logger.setLevel(logging.INFO)
        elif level in 'DEBUG':
            self._logger.setLevel(logging.DEBUG)
        return True

    def handle(self,method = 'PRINT',config = None):
     #   print (methode)
        if 'SYSLOG' in method:
          #  print('Ssyslog',config )
            host = config.get('LOGSERVER','localhost')
           # print('Syslog',host)
            handler = logging.handlers.SysLogHandler(address=(host, 514), facility=19)

            hostname = socket.gethostname()
            formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s'.format(hostname),'%b %e %H:%M:%S')
            handler.setFormatter(formatter)

        elif 'LOGFILE' in method:
            file = config.get('LOGFILE','./logger.log')
            handler = logging.FileHandler(file)
            formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s','%b %e %H:%M:%S')
            handler.setFormatter(formatter)

        else:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s', '%b %e %H:%M:%S')
            handler.setFormatter(formatter)


        self._logger.addHandler(handler)

        return True

    def get_logger(self):
        return self._logger

    def debug(self,msg):
    #    print('debug',msg)
        self._logger.debug(msg)

    def info(self,msg):
     #   print('info',msg)
        self._logger.info(msg)

    def warning(self,msg):
      #  print('warning',msg)
        self._logger.warning(msg)

    def error(self,msg):
       # print('error',msg)
        self._logger.error(msg)

    def critical(self,msg):
       # print('critical',msg)
        self._logger.critical(msg)



if __name__ == "__main__":
    logger = MyLogger()
    logger.handle('SYSLOG', {'HOST': '172.17.115.121'})
    logger.handle()
    logger.info("Hello, Logger")
    logger.debug("bug occured")

