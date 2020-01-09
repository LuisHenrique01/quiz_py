import pygame 
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from Tela import *
from Player import *

#t e objeto Tela
t = Tela()
pygame.init() #inicia Pygame

tela = t.criaTela("entrar") #criar tela inicial

nome = t.getName(tela)
p1 = Player(nome) #pega o nome e cria o player

#escolha de opcao
tela = t.criaTela("p1")
op = t.getOpcoes(tela)
p1.setOpcao(op)
if p1.getOpcao()  == "A":
    p1.setPontuacao(20)
    print("Nick: %s"%p1.getNome())
    print("Pontuação: %s"%p1.getPontuacao()) 
else:
    print('FFFF')

pygame.mixer.music.load('trilha.mp3')
pygame.mixer.music.play()
 
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()