from threading import Timer,Thread,Event
import os
import json


class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    os.system('rm remote_version.json')    # remote_version.json var ise silindi.
    os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json')
    #print('ipsem lorem')

bir_saniye = 1
bir_gün = 60*1440

t = perpetualTimer(bir_saniye*5,printer)
t.start()