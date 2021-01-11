from threading import Timer,Thread,Event
import os, os.path
import time, datetime
import json
import requests
from requests.exceptions import HTTPError


mesaj = '''
-----------------------------------------------------------------------
              Güncelleme kontrol sistemi
------------------------------------------------------------------------
'''
mesaj2 = '''
-------------------------------------------------------------------------
!!! Uzak depoya erişilemiyor lütfen internet bağlantınızı kontrol edin !!!
-------------------------------------------------------------------------
'''
mesaj3 = '''
-------------------------------------------------------------------------
                  Uzak depoya  başarıyla erişildi
                Güncelleme kontrol dosyası indirildi
-------------------------------------------------------------------------
'''
mesaj4 = '''
-------------------------------------------------------------------------
                  Uzak depoya erişim test ediliyor...
-------------------------------------------------------------------------
'''
#------------------- Zamanlayıcı ------------------------
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
      
#----------------- İnternet kontrol --------------------------------

def check_internet():
    print('---------------------------------------')
    print('İnternet bağlantısı kontrol ediliyor...')
    url='https://raw.githubusercontent.com/faruk21/frpi/main/version/local_version.json'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("İnternet bağlantısı yok.")
    return False
# Bu kısım belirlenen adrese bağlantı olduğunda True olmadığında False verir.
#-------------------------------------------------------------------

#--------------------- Tananımlamalar ------------------------------
remote_file = "remote_version.json"
local_file = "local_version.json"
yol = "./storage/shared/Python//Updater/frpi/version"
git_yolu = "/Updater/frpi"
r_path = os.path.join(yol, remote_file)
l_path = os.path.join(yol, local_file)
rv_yolu = "./Updater/frpi/version/remote_version.json" # remote version yolu
lv_yolu = "./Updater/frpi/version/local_version.json"
#----------------- Git Komutları ------------------------------------
git_add = 'git add .'
git_commit = "git commit -m 'a' "
git_pull = 'git pull --no-edit'
#------------------------------------------------------------------------------

def indirme():
    bağlantı_control = check_internet()              # İnternet bağlantı kontrolü.

    if bağlantı_control:                             # Eğer bağlantı varsa...
        print('Bağlantı kuruldu')
        if os.path.exists(rv_yolu):                  # Eğer rv_yolu içinde dosya varsa.
            os.remove(rv_yolu)                       # Eski remote dosyasını sil
            print("Eski remote dosyası silindi")
        else:
            print("Eski remote dosyası yok")
        try:
            r = requests.get('https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json')   # Dosyanın indirme testi
            r.raise_for_status()                                                                                  # Olumlu veya olumsuz sonuç
            os.system('wget  https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./Updater/frpi/version') # Olumlu ise dosyanın indirme işlemi.
            file_rw()
        except HTTPError:
            print('Dosya indirilemedi')    # İndirilememesi durumu
        else:
            pass
             #print('İndirme Başarılı')     # İndirilmesi durumu
    else:
        print(input("Lütfen internet bağlantınızı kontrol edip bir tuşa basın.")) # İnternet bağlantısı sorunu


def file_rw():
    print('-----------------------------------------------------------------')
    print('Lokal dosya kontrol ediliyor...')
    print('-----------------------------------------------------------------')
    if os.path.exists(rv_yolu):
        with open(rv_yolu, 'r') as f:
            remote_v = json.load(f)
            r_veriler = remote_v['versions']
            r_version = r_veriler[0]['version_number']
            
            l_version = local()
            #print(f'local: {l_version} remote: {r_version}')

            if r_version > l_version:
                with open(rv_yolu, 'r') as f, open(lv_yolu, 'w') as f2:
                    r_veriler = json.load(f)
                    json.dump(r_veriler, f2, indent=4)
                #os.chdir('./Updater/frpi')
                os.system(" git add . ")
                os.system("git commit -m 'güncelleme' ")
                os.system("git pull --no-edit")
                #os.system("git push ")
                print('-----------------------------------------------------------------')
                print(f'Güncelleme tamamlandı! version: {l_version}')
                print('-----------------------------------------------------------------')
                #input('bekle')

            else:
                print('-----------------------------------------------------------------')
                print(f'Program güncel! version: {l_version}')
                print('-----------------------------------------------------------------')
                #input('bekle')
    
    else:
        print('remote file dosyası bulunamadı.')
        indirme()


def local():
    for x in range(2):
        if os.path.exists(lv_yolu):
            with open(lv_yolu, 'r') as f:
                local_v = json.load(f)
                l_veriler = local_v['versions']
                l_version = l_veriler[0]['version_number']
                x = 2
        else:
            with open(rv_yolu, 'r') as f, open(lv_yolu, 'w') as f2:
                r_veriler = json.load(f)
                json.dump(r_veriler, f2, indent=4)
                print('Local dosya tekrar oluşturuldu.')
    return l_version

        




#-------------------------------------------------------------------------------------------------------
def update():
    indirme()


bir_dakika = 60*10
saniye = 2
t = perpetualTimer(bir_dakika,update)
print(mesaj)
t.start()
