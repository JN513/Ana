from gtts import gTTS  # biblioteca para criação de audio e tals
from subprocess import call  # para reproduzir audio no linux e mac
import vlc

# from playsound import playsound            #para reproduzir no windows


def cria_audio(audio, nome):
    tts = gTTS(audio, lang="pt-br")  # a menssagem do audio e a linguagem
    tts.save(f"audios/{nome}.mp3")  # salvando o audio
    # sinataxe o player e o audio
    # call(["ffplay", "-nodisp", "-autoexit", "audios/" + nome + ".mp3"])  # no linux
    p = vlc.MediaPlayer(f"audios/{nome}.mp3")
    p.play()
    # call(['afplay','audios/'+nome+'.mp3'])    #no mac
    # playsound('audios/'+nome+'.mp3')          #windows aqui so passa o audio


a = input("Digite a menssage do audio:\n")
b = input("Digite o nome do audio:\n")

cria_audio(a, b)
