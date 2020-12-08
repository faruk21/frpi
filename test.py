import os
import time

while True:
    girdi = input('Güncellemek istiyor musunuz? E/H :')

    if girdi == 'E':
        print('------------------- Güncelleme başlatılıyor -------------------')
        time.sleep(1)
        os.system('git status')
        print('---------------------------------------------------------------')
        os.system('git add .')
        os.system('git commit -m "test.txt düzenlendi"')
        print('Dosyalar yerel depoya eklendi.')
        print('---------------------------------------------------------------')
        os.system('git status')
        time.sleep(1)
        print('Dosyalar uzak depoya gönderiliyor...')
        os.system('git push')
        print('Dosyalar uzak depoya gönderildi...')
        print('Güncelleme başarılı.')
        print('---------------------------------------------------------------')
        break

    else:
        print('Güncelleme iptal edildi...')
        time.sleep(1)

#os.system('git')
