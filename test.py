import os
import json
import os.path

path = './Updater/frpi/'
  
# Check whether the specified 
# path exists or not 
print(os.path.exists(path))
#isExist = os.path.exists(path)
#print(isExist) 

# Specify path 
path2 = './Updater/frpi/remote_version.json'
  
# Check whether the specified 
# path exists or not 
test = os.path.exists(path2) 
print(test)


#os.system('rm remote_version.json')
os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json -P /root/Updater/')