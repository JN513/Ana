# -*- coding: utf-8 -*-
import speech_recognition as sr

def monitora_audio():
    microfone = sr.Recognizer() #pega o adio do microfone

    with sr.Microphone() as source:
        print("Estou aqui!!! Pode falar.")
        audio = microfone.listen(source)

    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    try:
        print(microfone.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
monitora_audio()
