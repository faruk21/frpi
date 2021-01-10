import os
import json
import os.path

local_dosya = "remote_version.json"
yol = "/root/Updater/version"

path = os.path.join(yol, local_dosya)
os.remove(path)
#os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json -P /root/Updater/version/')