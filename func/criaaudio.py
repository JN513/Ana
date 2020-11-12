# -*- coding: utf-8 -*-
from gtts import gTTS
from subprocess import call
#from playsound import playsound

def cria_audio(menssagem):
    tts = gTTS(menssagem, lang='pt-br')
    tts.save('audios/geral.mp3')
    print('\nANA: ',menssagem,'\n')
    call(['ffplay','-nodisp','-autoexit','audios/geral.mp3'])
    #playsound('audios/geral.mp3')          #windows aqui so passa o audio
