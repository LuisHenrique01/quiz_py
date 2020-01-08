import pygame 
from pygame.locals import *
from sys import exit

class Tela():
    def __init__(self):
        #self.screen = screen
        self.points = [1000, 800, 500, 100, 50]
        self.names = ["W.KAPPLER", "W.KAPPLER", "W.KAPPLER", "W.KAPPLER", "W.KAPPLER"]
        self.black = (0, 0, 0)
        self.font = None
        self.font2 = None
        self.clock = pygame.time.Clock()
        self.greets = "                                                       GREETS TO: ACHIM - ALINE - ANDI - ANJA - ANNE-CAROLE - ANTHONY - BENNI - CARLOS - CHRISTIAN - CHRISTOPH - CLUBHAUS GANG - COSMO - DANIEL - DEPOT GANG - DIMA - DOMINIK - DORO - ELI - EVA - FACE HUGGER - FARI - FAST - FELIX - FLO - FRANK - GINTI - HEINER - HENNING - JAN - JARED - JENS - JOJO - JULIA - JULIUS - KARIN - KATRIN - LISA - LUIZ - MARKUS - MASTER BLASTER - MATZE - MICHI - MILO - NICI - QARC - PIT - RALF - SABINE - SANDRA - SANDY - SCHMID SISTERS - SHANTHY - SILVERSTAR - SIMON - STEFAN - STEFFI - THOMAS - UDO - VOLKI - WALDMEISTER - YANG - ZAPHOLD - ZED - ZEROZERO"
        self.greetsPos = 0
    
    def telaInicial(self):
        img = pygame.image.load("entrar.png")
        tela = pygame.display.set_mode((1239, 860), 0, 32)
        tela.fill((255,255,255))
        pygame.display.set_caption("QUIZ_PY")
        #pygame.draw.rect(tela,(255,0,0),(100,200,200,100))
               
        tela.blit(img, (0, 0))
        pygame.display.flip()
        return tela
    
    def texto(self, tela, mensagem, posicao, cor, tam):
        arial = pygame.font.SysFont('arial', tam)
        mens = arial.render(mensagem, True, cor, 0)
        tela.blit(mens, posicao)
        
    def getName(self, screen):
        name = ""
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if event.key != pygame.K_SPACE:
                            c = pygame.key.name(event.key).upper()
                            if len(name) < 10:
                                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:-+":
                                    name += c
        return name