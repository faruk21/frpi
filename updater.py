from threading import Timer,Thread,Event
import os, os.path
import time, datetime
import json

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
      
#-------------------------------------------------------

remote_file = "remote_version.json"
local_file = "local_version.json"
yol = "./storage/shared/Python//Updater/frpi/version"
git_yolu = "/Updater/frpi"
r_path = os.path.join(yol, remote_file)
l_path = os.path.join(yol, local_file)
git_add = 'git add .'
git_commit = "git commit -m 'a' "
git_pull = 'git pull --no-edit'

remote_yolu = "./storage/shared/Python/Updater/frpi/version/remote_version.json"

#os.path.exists('/home/istihza/Desktop/falanca.txt')

def update():
    print(mesaj4)
    for x in range(2):
        if os.path.exists(remote_yolu):
            os.remove(remote_yolu)
            print("dosya silindi")
        else:
            print("Eski remote dosyası yok")
        
        try:
            os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./storage/shared/Python/Updater/frpi/version')
            
        except FileNotFoundError:
            print("indirilemedi")

def l_file_cntrl():
    print('-----------------------------------------------------------------')
    print('Lokal dosya kontrol ediliyor...')
    print('-----------------------------------------------------------------')
    try:
        with open(l_path, 'r') as f:
            local_v = json.load(f)
            l_veriler = local_v['versions']
            l_version = l_veriler[0]['version_number']
            print(f'Local dosya başarıyla okundu: {l_version}')
        
    except FileNotFoundError:
        #print('-----------------------------------------------------------------')
        #print('local file dosyası bulunamadı, yeniden oluşturuluyor...')
        with open(r_path, 'r') as f, open(l_path, 'w') as f2:
            veri = json.load(f)
            json.dump(veri, f2, indent=4)
            print("Locaf file tekrar oluşturuldu")



#-------------------------------------------------------------------------------------------------------
bir_dakika = 60
saniye = 2
t = perpetualTimer(saniye,update)
print(mesaj)
t.start()
