import os
import time

mesaj = '''
---------------------------------------------------------------
              Güncelleme kontrol sistemi
---------------------------------------------------------------
'''
def remote_r():
    remote = open('remote_version.txt', 'r')
    remote_vers = remote.read() 
    return remote_vers

def localv_r():
    old = open('local_version.txt', 'r')
    local_vers = old.read()
    return local_vers

def localv_w(newv):
    localv = open('local_version.txt', 'w')           # local_version.txt dosyası yazma modunda açıldı.
    localv.write(newv)

#-------------------------------------------------------------------------------------------------------

def update_control():                    
    print('Güncelleme kontrol dosyası indiriliyor.')
    print('-----------------------------------------------------------------')
    os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.txt')
    print('-----------------------------------------------------------------')
    print('Güncelleme kontrol dosyası indirildi.')
    print('Güncelleme kontrol dosyası okunuyor.')
    print('---------------------------------------------------------------')
    remoteread = remote_r()
    localread = localv_r()
    print(f'Local sürüm: {localread}')
    print(f'serverdaki sürüm: {remoteread}')
    print('---------------------------------------------------------------')
    print('Local sürüm güncelleniyor')
    #localv_w(remoteread)
    print(f'Yeni local sürüm: {remoteread}')
    #os.system('rm remote_version.txt')                # remote_version.txt'silindi.
    print('remote_version.txt silindi')
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
    print(mesaj)
    update_control()  
    break

