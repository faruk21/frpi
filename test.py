import os
import time

mesaj = '''
Güncelleme almak istiyor musunuz? e/h:
Çıkmak için 'c'
---------------------------------------------------------------
Komut: 

'''
while True:


#os.system('git')

    def test():
        os.system('git fetch')
        my_file = open('version.txt', 'r')
        version = my_file.read()

        print(version)

