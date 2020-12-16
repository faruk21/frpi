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
        #print(server)
        #print(local)
        if server == local:
            print('Program zaten güncel')
            os.system('rm remote_version.json')
            break
        else:
            with open('remote_version.json', 'r') as f:
                remote_v = json.load(f)

            print('Local sürüm güncelleniyor...')

            with open('local_version.json', 'w') as f:
                json.dump(remote_v, f, indent=4)

            local = local_json_read()
            if server == local:
                print(f'Güncelleme işlemi başarılı, yeni local sürüm: {local} ')
                os.system('rm remote_version.json')
                break


def filecontrol():
    print(mesaj4)
    for x in range(3):
        try:
            os.system('rm remote_version.json')
            os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json')
            with open('remote_version.json', 'r') as f:
                local_v = json.load(f)
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
        local_v = json.load(f)
        veriler = local_v['versions']
        
        l_version = veriler[0]['version_number']
        gün = veriler[0]['day']
        ay = veriler[0]['month']
        yıl = veriler[0]['year']
        #print(gün,ay,yıl)
        return l_version
        


def remote_json_read():
    with open('remote_version.json', 'r') as f:
        remote_v = json.load(f)
        veriler = remote_v['versions']
        
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
        local_json_w()
        #print('remote_version.txt silindi')
        print('---------------------------------------------------------------') 

while True:
    print(mesaj)
    update_control()
    break

