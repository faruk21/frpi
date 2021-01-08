import datetime
import os

endTime = datetime.datetime.now() + datetime.timedelta(seconds=1)
while True:
   if datetime.datetime.now() >= endTime:
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=5)

   try:
      os.chdir("frpi")
      os.system('python3 updater.py')

   except FileExistsError:
      print("error")