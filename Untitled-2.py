

import re

soal1 = "Saat meng*ecat tembok, Agung dib_antu oleh Raihan"
soal2 = "Berapa u(mur minimal[ untuk !mengurus ktp?"
soal3 = "Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda"

def checkWord(word):
    bad_character = ['[',']']
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:=]')
    test = 0 
    print(word.split())

    for i in word.split() :
        if(regex.search(i) == None):
            print(i)
            test = test + 1

    print(test)
checkWord(soal3)