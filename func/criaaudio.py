# -*- coding: utf-8 -*-
from gtts import gTTS
from subprocess import call

def cria_audio(menssagem):
    tts = gTTS(menssagem, lang='pt-br')
    tts.save('audios/geral.mp3')
    print('\nANA: ',menssagem,'\n')
    call(['ffplay','-nodisp','-autoexit','audios/geral.mp3'])
