import os
import json
import os.path

remote_file = "remote_version.json"
yol = "/root/Updater/version"

path = os.path.join(yol, remote_file)
#os.remove(path)
os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json -P /root/Updater/version/')