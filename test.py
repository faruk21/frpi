import os
import time

mesaj = '''
Güncelleme almak istiyor musunuz? e/h:
Çıkmak için 'c'
---------------------------------------------------------------
Komut: 

'''
print('güncelleme kontrol dosyası alınıyor')
os.system('git fetch')
os.system('git pull')

#my_file = open('version.txt', 'r')
#version = my_file.read()

#print(version)

