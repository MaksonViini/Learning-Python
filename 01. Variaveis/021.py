#Tocando um MP3
from pygame import mixer
mixer.init()
mixer.music.load('EX021.mp3') #Adicione o nome da musica
mixer.music.play()