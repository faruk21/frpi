import os
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
def update():
    print(mesaj4)
    for x in range(3):           # Bu işlemi 3 kez dene.
        try:
            os.chdir("frpi")    #frpi dizinine geçildi.
            os.system('rm remote_version.json')    # remote_version.json var ise silindi.
            os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.json')   # remote_version.json indirilmesi deneniyor.

            
            with open('remote_version.json', 'r') as f:
                remote_v = json.load(f)
                r_veriler = remote_v['versions']
                r_version = r_veriler[0]['version_number']
            #r_gün = veriler[0]['day']
            #r_ay = veriler[0]['month']
            #r_yıl = veriler[0]['year']
            print(mesaj3)   # Uzak depoya  başarıyla erişildi Güncelleme kontrol dosyası indirildi.

            l_version = l_file_cntrl()

        except FileNotFoundError:
            #print('-----------------------------------------------------------------')
            if x == 2:
                print(mesaj2,x)
            #print('internet veya dosya sorunu')
        

def l_file_cntrl():
    print('Lokal dosya kontrol ediliyor...')
    print('-----------------------------------------------------------------')
    try:
        with open('local_version.json', 'r') as f:
            local_v = json.load(f)
            v_veriler = local_v['versions']
            l_version = v_veriler[0]['version_number']

    except FileNotFoundError:
        print('-----------------------------------------------------------------')
        print('local file dosyası bulunamadı, yeniden oluşturuluyor...')
        with open('remote_version.json', 'r') as f, open('local_version.json', 'w') as f2:
            veri = json.load(f)
            json.dump(veri, f2, indent=4)
    return l_version

def test():
    time.sleep(5)
    print('deneme1')
    print('deneme2')
    

#-------------------------------------------------------------------------------------------------------
while True:
    print(mesaj)
    update()
    break
'''
    print(mesaj)
    update()
    break
'''