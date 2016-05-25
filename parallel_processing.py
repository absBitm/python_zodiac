# https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=run%20two%20process%20parallel%20in%20python
# http://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel

from multiprocessing import Process
import time
from twisted.internet import reactor
from loggers import sensor_logger

def func1():
  print 'func1: starting' , time.time()
  # suscribe(to_msg) or reply(to_request)
  # do your task 
  # print 'func1: finishing', time.time()
  func2('eg. log request came')
  for i in xrange(10000000): pass
  reactor.run()

def func2(msg='wassup'):
  print 'func2: starting' , time.time() , ' message : ' , msg
  # do your task 
  # communication can be done via pipe/queue queue , queue has genralised appliaction handlers than pipe .
  # publish(msg) to suscribers with (unique topic e.g log) or (request/reply)  pub sub is better .
      
  print 'func2: finishing' ,time.time()


def runInParallel(*functions):
  proc = []
  for fi in functions:
    p = Process(target=fi)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

if __name__ == '__main__':
  # run processes as parallel 
  runInParallel(func1, func2)

