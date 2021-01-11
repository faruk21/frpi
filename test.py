import os
import json
import os.path
import time

remote_yolu = "./storage/shared/Python/Updater/frpi/version/remote_version.json"

print(os.path.exists(remote_yolu))

if os.path.exists(remote_yolu):
    print("Dosya var.")
else:
    print("dosya yok.")
'''
remote_file = "remote_version.json"
yol = "./Updater/frpi/version/"

path = os.path.join(yol, remote_file)
#os.remove(path)
'''
#os.chdir('./storage/shared/Python/Updater/frpi/version')
#os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./storage/shared/Python/Updater/frpi/version/')
#os.system("ls")


#os.remove("Updater/frpi/version/remote_version.json")
'''
git_add = 'git add .'
git_commit = "git commit -m 'a' "
git_pull = 'git pull --no-edit'
git_push = 'git push'

os.system('ls')
os.chdir('./storage/shared/Python/Updater/frpi')
os.system(git_add)
os.system(git_commit)
os.system(git_push)
os.system('cd')
'''