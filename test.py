import os
import json
import os.path
import time
import requests

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
#os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./storage/shared/Python/Updater/frpi/version')
#os.system("ls")


#os.remove("Updater/frpi/version/remote_version.json")
def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("İnternet bağlantısı yok.")
    return False
    
test = check_internet()
print(test)
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



                with open(l_path, 'r') as f:
                    local_v = json.load(f)
                    l_veriler = local_v['versions']
                    l_version = l_veriler[0]['version_number']
    
                if round(r_version,1) > l_version:
                    print(f'güncelleme mevcut local: {l_version} remote: {round(r_version,1)}')
                    with open(r_path, 'r') as f, open(l_path, 'w') as f2:
                        veri = json.load(f)
                        json.dump(veri, f2, indent=4)
                    with open (l_path, 'r') as f2:
                        local_v = json.load(f2)
                        l_veriler = local_v['versions']
                        l_version = l_veriler[0]['version_number']

# git pull origin master
# remote dan kodlarınızı local ortamınıza çekersiniz, default kendiliğinden merge işlemini yapar.
# pull a benzer şekilde fetch  remote daki kodların kopyasını local e oluşturur, ancak  merge yapmaz.
# 18:10
                
                os.chdir('./storage/shared/Python/Updater/frpi')
                os.system(git_add)
                os.system(git_commit)
                os.system(git_pull)
                os.system('cd')
                print('---------------------------------------------------')
                print(f"Güncelleme tamamlandı, güncel version: {l_version}")

                else:
                    print("Program zaten güncel")
'''
