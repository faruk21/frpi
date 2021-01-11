import os
import json
import os.path
'''
print(os.path.exists("/root/Updater/frpi/version/remote_version.json"))

remote_file = "remote_version.json"
yol = "./Updater/frpi/version/"

path = os.path.join(yol, remote_file)
#os.remove(path)
os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./Updater/frpi/version/')
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
os.chdir('./storage/shared/Python')
os.system('ls')