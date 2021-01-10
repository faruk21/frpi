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

remote_file = "remote_version.json"
local_file = "local_version.json"
yol = "./Updater/frpi/version"
r_path = os.path.join(yol, remote_file)
l_path = os.path.join(yol, local_file)

def update():
    print(mesaj4)
    for x in range(1):           # Bu işlemi 3 kez dene.
        try:
            print("silme deneniyor")
            os.remove(r_path)
            os.system("ls")
            print("silindi")
            os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/version/remote_version.json -P ./Updater/frpi/version/')
            
            with open(r_path, 'r') as f:
                remote_v = json.load(f)
                r_veriler = remote_v['versions']
                r_version = r_veriler[0]['version_number']
            #r_gün = veriler[0]['day']
            #r_ay = veriler[0]['month']
            #r_yıl = veriler[0]['year']
            #print(mesaj3)   # Uzak depoya  başarıyla erişildi Güncelleme kontrol dosyası indirildi

            l_file_cntrl()

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
                os.system('git add .')
                os.system("git commit -m 'a' ")
                os.system('git pull --no-edit')
                print('---------------------------------------------------')
                print(f"Güncelleme tamamlandı, güncel version: {l_version}")

            else:
                print("Program zaten güncel")

        except FileNotFoundError:
            #print('-----------------------------------------------------------------')
            if x == 2:
                print(mesaj2,x)
            #print('internet veya dosya sorunu')
        
        

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
saniye = 10
t = perpetualTimer(saniye,update)
print(mesaj)
t.start()

#
