import os
import time
import json


mesaj = '''
-----------------------------------------------------------------------
              Güncelleme kontrol sistemi
------------------------------------------------------------------------
'''
mesaj2 = '''
-------------------------------------------------------------------------
!!! Uzak depoya erişilemiyor lütfen internet bağlntınızı kontrol edin !!!
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
def remote_r():
    print('---------------------------------------------------------------')
    remote = open('remote_version.txt', 'r')
    remote_vers = remote.read() 
    #print(remote_vers)
    return remote_vers

def localv_r():
    old = open('local_version.txt', 'r')
    local_vers = old.read()
    return local_vers

def localv_w():
    print('Local sürüm kontrol ediliyor')
    for x in range(3):
        server = remote_r()
        local = localv_r()
        print(server)
        print(local)
        if float(server) == float(local):
            print('Program zaten güncel')
            break
        else:
            localv = open('local_version.txt', 'w')           # local_version.txt dosyası yazma modunda açıldı.
            localv.write(server)

            float_server = float(server)
            float_local = float(local)
            if float_server == float_local:
                print(f'Güncelleme işlemi başrılı, yeni local sürüm: {local} ')
                os.system('rm remote_version.txt')
                break

def filecontrol():
    print(mesaj4)
    for x in range(3):
        try:
            os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.txt')
            f = open('remote_version.txt')
            sonuc = True
            print(mesaj3)
            break
        except FileNotFoundError:
            sonuc = False
            print('-----------------------------------------------------------------')
    if x == 2:
        print(mesaj2)
    return sonuc

def json_read():
    with open('remote_version.json', 'r') as f:
        cıktı = json.load(f)
    for i in cıktı['versions']:
        print(i['tarih'])

#-------------------------------------------------------------------------------------------------------

def update_control():
    control = filecontrol()
    if control == True:
        print('---------------------------------------------------------------')
        localv_w()
        #print('remote_version.txt silindi')
        print('---------------------------------------------------------------') 

def hesap():
    sonuc = time.time() - starttime
    print(sonuc)
    #print('hesap çalışıyor')

    if sonuc > 5:
        print('işlkjhgf')
        sonuc = time.time()
        güncelleme(old)

while True:
    #os.system('rm remote_version.txt')
    #print(mesaj)
    #update_control()
    json_read()
    break

