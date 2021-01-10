import os
import json
import os.path

print(os.path.exists("/root/Updater/frpi/version/remote_version.json"))

remote_file = "remote_version.json"
yol = "./Updater/frpi/version/"

path = os.path.join(yol, remote_file)
#os.remove(path)
os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./Updater/frpi/version/')
#os.system("ls")
#os.remove("Updater/frpi/version/remote_version.json")