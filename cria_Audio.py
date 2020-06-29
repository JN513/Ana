from gtts import gTTS                       #biblioteca para criação de audio e tals
from subprocess import call                 #para reproduzir audio no linux e mac
#from playsound import playsound            #para reproduzir no windows

def cria_audio(audio,nome):
    tts = gTTS(audio, lang='pt-br')         #a menssagem do audio e a linguagem
    tts.save('audios/'+nome+'.mp3')         #salvando o audio
    #sinataxe o player e o audio
    call(['aplay','audios/'+nome+'.mp3'])   #no linux
    #call(['afplay','audios/hello.mp3'])    #no mac
    #playsound('audios/hello.mp3')          #windows aqui so passa o audio

a = input('Digite a menssage do audio:')
b = input('Digite o nome d audio:')
cria_audio(a,b)
