# -*- coding: utf-8 -*-
from gtts import gTTS
from subprocess import call
import vlc

# from playsound import playsound


def cria_audio(menssagem):
    tts = gTTS(menssagem, lang="pt-br")
    while True:
        try:
            tts.save("audios/geral.mp3")
            break
        except:
            print("Erro ao gerar audio!!!")
    print(f"\nANA: {menssagem}\n")
    p = vlc.MediaPlayer("audios/geral.mp3")
    p.play()
    # call(["ffplay", "-nodisp", "-autoexit", "audios/geral.mp3"])
    # playsound('audios/geral.mp3')          #windows aqui so passa o audio
