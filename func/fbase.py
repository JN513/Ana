# -*- coding: utf-8 -*-
from datetime import time, datetime, timezone, timedelta
from subprocess import call
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser
from func import criaaudio
import json

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias =  BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:#trocando o numero muda quantas noticas passa
        menssagem = item.title.text
        criaaudio.cria_audio(menssagem)

def hora():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%H:%M')
    criaaudio.cria_audio(data_e_hora_sao_paulo_em_texto)

def data():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y')
    criaaudio.cria_audio(data_e_hora_sao_paulo_em_texto)

def dataehora():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
    criaaudio.cria_audio(data_e_hora_sao_paulo_em_texto)

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

def previsao_tempo(tempo=False, minimax=False, todos=False):
    site = get('https://api.openweathermap.org/data/2.5/weather?q=Guap%C3%A9,mg,br&appid=d489d1a675d0a5e9990e3086d3cbe78b&units=metric&lang=pt')
    clima = site.json()
    #print(json.dumps(clima, indent=4))
    temperatura = clima['main']['temp']
    temperaturamin =clima['main']['temp_min']
    temperaturamax = clima['main']['temp_max']
    umidade = clima['main']['humidity']
    descricao =clima['weather'][0]['description']

    if todos:
        menssagem = f'hoje fara em média {temperatura} graus, com minimas de {temperaturamin} graus e máximas de {temperaturamax}graus, humidade de {umidade}% e {descricao}'
        criaaudio.cria_audio(menssagem)
    elif tempo:
        menssagem = f'No momento fazem {temperatura} graus, a humidade esta em cerca de {umidade}% e {descricao}'
        criaaudio.cria_audio(menssagem)
    elif minimax:
        menssagem = f'Minima de {temperaturamin} graus, maxima de {temperaturamax} graus'
        criaaudio.cria_audio(menssagem)

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

def status_covid(pedido):
    if 'brasil' in pedido:
        site = get('https://covid19-brazil-api.now.sh/api/report/v1/brazil')
        dados = site.json()

        confirmados = dados['data']['confirmed']
        mortos = dados['data']['deaths']
        suspeitos = dados['data']['recovered']
        atualizadoem = dados['data']['updated_at']

        menssagem = f' Atualmente no Brasil tem {confirmados} casos confirmados, {suspeitos} recuperados e {mortos} mortes confirmadas por covid-19.'

        criaaudio.cria_audio(menssagem)

    elif 'minas gerais' in pedido:
        site = get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/mg')
        dados = site.json()

        confirmados = dados['cases']
        mortos = dados['deaths']
        suspeitos = dados['suspects']
        recuperados = dados['refuses']
        atualizadoem = dados['datetime']

        menssagem = f'Atualmente em Minas-Gerais tem {confirmados} casos confirmados, {suspeitos} suspeitos e {mortos} mortes confirmadas por covid-19.'

        criaaudio.cria_audio(menssagem)

    elif 'estados' in pedido:
        site = get('https://covid19-brazil-api.now.sh/api/report/v1')
        dados = site.json()

        for i in range(0,25):
            confirmados = dados['data'][i]['cases']
            mortos = dados['data'][i]['deaths']
            suspeitos = dados['data'][i]['suspects']
            recuperados = dados['data'][i]['refuses']
            atualizadoem = dados['data'][i]['datetime']
            estado = dados ['data'][i]['state']

            menssagem = f'{estado} Atualmente tem {confirmados} casos confirmados, {suspeitos} suspeitos e {mortos} mortes confirmadas por covid-19.'

            criaaudio.cria_audio(menssagem)
