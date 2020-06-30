# -*- coding: utf-8 -*-
import speech_recognition as sr

def monitora_audio():
    microfone = sr.Recognizer() #pega o adio do microfone

    with sr.Microphone() as source:
        print("Estou aqui!!! Pode falar.")
        audio = microfone.listen(source)

        try:
            print("Voce disse " + microfone.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

monitora_audio()
