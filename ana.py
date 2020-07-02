# -*- coding: utf-8 -*-
import speech_recognition as sr
from subprocess import call
from func import fbase
from func import criaaudio

##### configurações #####

hotword = 'ana'
with open('config/sistema-intelige-1537185170980-b86ebc917520.json') as credenciais_google:
    credenciais_google = credenciais_google.read()

##### funções principais #####

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            print("Estou aqui: ")
            audio = microfone.listen(source)

            try:

                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('Comando: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    #break

            except sr.UnknownValueError:
                print("Google not understand audio")
                #responde('naoentende')

            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
                responde('errodeconecao')

    return trigger

def responde(arquivo):
    call(['ffplay','-nodisp','-autoexit','audios/'+arquivo+'.mp3'])

def executa_comandos(trigger):
    if 'notícias' in trigger:
        fbase.ultimas_noticias()
    elif 'hora' in trigger:
        fbase.hora()
    elif 'data' in trigger:
        fbase.data()
    elif 'data' in trigger and 'hora' in trigger:
        fbase.dataehora()
    elif 'toca' in trigger:
        album = trigger.strip(hotword)
        fbase.playlist(album)
    elif 'abra' in trigger:
        nome = trigger.strip(hotword)
        fbase.abre_pagina(nome)
    elif 'abrir' in trigger:
        nome = trigger.strip(hotword)
        fbase.abre_pagina(nome)
    elif 'tempo' in trigger and 'agora' in trigger:
        fbase.previsao_tempo(tempo=True)
    elif 'temperatura' in trigger and 'hoje' in trigger:
        fbase.previsao_tempo(minimax=True)
    elif 'clima' in trigger:
        fbase.previsao_tempo(todos=True)
    else:
        menssagem = trigger.strip(hotword)
        if menssagem != "":
            criaaudio.cria_audio(menssagem)
            print('Comando inválido ', menssagem)
            responde('comanin')
        else:
            reponde('hello')

##### função inicio #####

def main():
    monitora_audio()

main()
