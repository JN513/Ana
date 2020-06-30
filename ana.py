# -*- coding: utf-8 -*-
import speech_recognition as sr

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
                    ### fazer algo ###
                    break
            except sr.UnknownValueError:
                print("Google not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))


monitora_audio()
