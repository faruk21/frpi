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
def local_json_w():
    print('Local sürüm kontrol ediliyor')
    for x in range(3):
        server = remote_json_read()
        local = local_json_read()
        print(server)
        print(local)

        if server == local:
            print('Program zaten güncel')
            break
        else:
            print('güncel değil')
            '''
            localv = open('local_version.txt', 'w')           # local_version.txt dosyası yazma modunda açıldı.
            localv.write(server)

            float_server = float(server)
            float_local = float(local)
            if float_server == float_local:
                print(f'Güncelleme işlemi başrılı, yeni local sürüm: {local} ')
                os.system('rm remote_version.txt')
                break
            '''

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

def local_json_read():
    with open('local_version.json', 'r') as f:
        remote_v = json.load(f)
        veriler = remote_v['versions']

        l_version = veriler[0]['version_number']
        gün = veriler[0]['day']
        ay = veriler[0]['month']
        yıl = veriler[0]['year']
        #print(gün,ay,yıl)
        return l_version


def remote_json_read():
    with open('remote_version.json', 'r') as f:
        local_v = json.load(f)
        veriler = local_v['versions']
        
        r_version = veriler[0]['version_number']
        r_gün = veriler[0]['day']
        r_ay = veriler[0]['month']
        r_yıl = veriler[0]['year']
        #print(gün,ay,yıl)
        return r_version

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
    local_json_w()

    break

