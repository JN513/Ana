#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
from subprocess import call
from func import fbase
from func import criaaudio
import json
from playsound import playsound
import vlc

##### configurações #####


config = open("config/config.json", "r")
config_json = json.load(config)

hotword = config_json["hotword"]
idioma = config_json["language"]

with open(
    "config/sistema-intelige-1537185170980-b86ebc917520.json"
) as credenciais_google:
    credenciais_google = credenciais_google.read()

##### funções principais #####


def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            microfone.adjust_for_ambient_noise(source)
            print("Estou aqui: ")
            audio = microfone.listen(source)

            try:

                trigger = microfone.recognize_google_cloud(
                    audio, credentials_json=credenciais_google, language=idioma
                )
                trigger = trigger.lower()

                if hotword in trigger:
                    print("Comando: ", trigger)
                    responde("feedback")
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google not understand audio")
                # responde('naoentende')

            except sr.RequestError as e:
                print(
                    "Could not request results from Google Cloud Speech service; {0}".format(
                        e
                    )
                )
                responde("errodeconecao")

    return trigger


def responde(arquivo):
    p = vlc.MediaPlayer(f"audios/{arquivo}.mp3")
    p.play()
    # call(["ffplay", "-nodisp", "-autoexit", f"audios/{arquivo}.mp3"])
    # playsound('audios/'+arquivo+'.mp3')          #windows aqui so passa o audio


def executa_comandos(trigger):
    if "notícias" in trigger:
        fbase.ultimas_noticias()
    elif "hora" in trigger:
        fbase.hora()
    elif "data" in trigger:
        fbase.data()
    elif "data" in trigger and "hora" in trigger:
        fbase.dataehora()
    elif "toca" in trigger or "toque" in trigger:
        album = trigger.strip(hotword)
        fbase.playlist(album)
    elif "abra" in trigger or "abrir" in trigger or "abre" in trigger:
        nome = trigger.strip(hotword)
        fbase.abre_pagina(nome)
    elif "coronavírus" in trigger or "covid" in trigger:
        nome = trigger.strip(hotword)
        fbase.status_covid(nome)
    elif "tempo" in trigger and "agora" in trigger:
        fbase.previsao_tempo(tempo=True)
    elif "temperatura" in trigger and "hoje" in trigger:
        fbase.previsao_tempo(minimax=True)
    elif "previsão" in trigger and "tempo" in trigger:
        fbase.previsao_tempo(todos=True)
    elif "liga a lâmpada" in trigger or "ativa a lâmpada" in trigger:
        fbase.publica_mqtt("rele/", "2")
    elif (
        "desativa a lâmpada" in trigger
        or "desliga a lâmpada" in trigger
        or "apaga a lâmpada" in trigger
    ):
        fbase.publica_mqtt("rele/", "3")
    elif "temperatura" in trigger:
        fbase.le_temperatura("sala1/temp/")
    elif "umidade" in trigger:
        fbase.le_umidade("sala1/umi/")
    elif "parar" in trigger and "execução" in trigger:
        print("parado Ana")
    else:
        menssagem = trigger.strip(hotword)
        criaaudio.cria_audio(menssagem)
        print("Comando inválido ", menssagem)
        responde("comanin")


##### função inicio #####


def main():
    responde("init")
    while True:
        try:
            monitora_audio()
        except:
            print("Erro ao executar o codigo")


if __name__ == "__main__":
    main()
