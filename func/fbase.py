# -*- coding: utf-8 -*-
from datetime import time, datetime, timezone, timedelta
from subprocess import call
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser
import criaaudio

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias =  BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:#trocando o numero muda quantas noticas passa
        menssagem = item.title.text
        caudio.cria_audio(menssagem)

def hora():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
    caudio.cria_audio(data_e_hora_sao_paulo_em_texto)

def playlist(album):
    if 'agora' in album:
        browser.open_new_tab('https://open.spotify.com/playlist/16LIDJwa7vtndNmXw7BJZ5?si=XL0vwvC8Q9-9c3PQRnQsxQ') #so o open abre janela
    elif 'flow' in album:
        browser.open_new_tab('https://open.spotify.com/show/3V5LBozjo4vNg2oJoA4Wb2?si=zpTFt8QfTjeGnHeAEdz3Ew')
    elif 'rock' in album:
        browser.open_new_tab('https://open.spotify.com/track/1Mf27cnAF1Q6Ko83XTM5d1?si=f1LVtboZS3CeF6LBbQzI7A')
    elif 'pop' in album:
        browser.open_new_tab('https://open.spotify.com/track/738SQjONa0q63yhLxvg3m1?si=gzQctUONSh2PU-O3PIFMUg')
    else:
        browser.open_new_tab('https://open.spotify.com/track/4u7EnebtmKWzUH433cf5Qv?si=QABP8IHuQv-Bg9R7qtC8Fg')

def abre_pagina(nome):
    if 'whatsapp' in nome:
        browser.open_new_tab('https://web.whatsapp.com/')
    elif 'github' in nome:
        browser.open_new_tab('https://github.com/JN513')
    elif 'presencial' in nome:
        browser.open_new_tab('https://presencial.muz.ifsuldeminas.edu.br/')
    elif 'youtube' in nome:
        browser.open_new_tab('https://www.youtube.com/')
    elif 'codify' in nome:
        browser.open_new_tab('http://codify.games/')

hora()
