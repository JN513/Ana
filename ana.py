# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
from datetime import time, datetime, timezone
from subprocess import call
from requests import get
from bs4 import BeautifulSoup
#from playsound import playsound            #para reproduzir no windows

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
                    break

            except sr.UnknownValueError:
                print("Google not understand audio")
                #responde('naoentende')

            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
                responde('errodeconecao')

    return trigger   

def responde(arquivo):
    call(['ffplay','-nodisp','-autoexit','audios/'+arquivo+'.mp3'])

def cria_audio(menssagem):
    tts = gTTS(menssagem, lang='pt-br')  
    tts.save('audios/geral.mp3')
    print('ANA: ',menssagem)
    call(['ffplay','-nodisp','-autoexit','audios/geral.mp3'])   #no linux
    #call(['afplay','audios/'+nome+'.mp3'])    #no mac
    #playsound('audios/'+nome+'.mp3')          #windows aqui so passa o audio

def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()
    elif 'hora' in trigger:
        hora()
    else:
        menssagem = trigger.strip(hotword)
        cria_audio(menssagem)
        print('Comando inválido ', menssagem)
        responde('comanin')
    

##### funções de comandos #####

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias =  BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:#trocando o numero muda quantas noticas passa
        menssagem = item.title.text
        cria_audio(menssagem)

def hora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    cria_audio(data_e_hora_em_texto)

def playlist():

##### função inicio #####

def main():
    monitora_audio()

main()
