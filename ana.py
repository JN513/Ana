# -*- coding: utf-8 -*-
import speech_recognition as sr

#####config#####
with open('sistema-intelige-1537185170980-b86ebc917520.json') as credenciais_google:
    credenciais_google = credenciais_google.read()

def monitora_audio():
    microfone = sr.Recognizer() #pega o adio do microfone

    with sr.Microphone() as source:
        print("Estou aqui!!! Pode falar.")
        audio = microfone.listen(source)

    try:
        print("Voce disse" + microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR'))
    except sr.UnknownValueError:
        print("Não consegui ouvir o audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


monitora_audio()
