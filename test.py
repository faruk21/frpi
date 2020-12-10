import os
import time

mesaj = '''
---------------------------------------------------------------
              Güncelleme kontrol sistemi
---------------------------------------------------------------
'''
def old_vers_r():
    old = open('local_version.txt', 'r')
    eski_vers = old.read()
    old.close()

    '''
    print('-----------------------------------------------------------------')
    print(f'Eski version: {eski_vers}')
    print('-----------------------------------------------------------------')
    '''

def old_vers_w(newv):
    localv = open('local_version.txt', 'w')           # local_version.txt dosyası yazma modunda açıldı.
    localv.write(newv)                                # newv'ye gelen veri local_version.txt dosyasına yazıldı.

def update_control():
    old_vers_r()
    print('Güncelleme kontrol ediliyor.')
    os.system('wget https://raw.githubusercontent.com/faruk21/frpi/main/remote_version.txt')

    with open('remote_version.txt', 'r') as rm_file:  # İndirilen remote_version.txt yazma modunda açıldı.
        rm_vrsn = rm_file.read()                      # remote_version.txt okundu rm_vrsn ye kaydedildi.
    print('---------------------------------------------------------------')
    print(f'Uzak depo version: {rm_vrsn}')
    #os.system('rm remote_version.txt')
    '''
    old = open('local_version.txt', 'r')
    eski_vers = old.read()
    old.close()
    print(f'Local version: {eski_vers}')                
    old_vers_w(rm_vrsn)                               # rm_vrsn old_vers'e gönderildi.
    os.system('rm remote_version.txt')                # remote_version.txt'silindi.
    print('---------------------------------------------------------------')  
    '''  

'''
    os.system('git fetch')
    os.system('git pull')
    my_file = open('version.txt', 'r')

def hesap():
    sonuc = time.time() - starttime
    print(sonuc)
    #print('hesap çalışıyor')

    if sonuc > 5:
        print('işlkjhgf')
        sonuc = time.time()
        güncelleme(old)
'''

while True:
    print(mesaj)
    update_control()  
    break

