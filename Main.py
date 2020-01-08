import pygame 
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from Tela import *

t = Tela()
pygame.init()

pygame.mixer.music.load('trilha.mp3')
#pygame.mixer.music.set_volume()
pygame.mixer.music.play()

tela = t.criaTela("entrar")
nome = t.getName(tela)
#tela = t.test(nome)
tela = t.criaTela("p1")

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()