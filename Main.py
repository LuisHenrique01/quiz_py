import pygame 
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from Tela import *

t = Tela()
pygame.init()
telaInicial = t.telaInicial()
nome = t.getName(telaInicial)
print(nome)
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()