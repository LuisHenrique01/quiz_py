import pygame 
from pygame.locals import *
from sys import exit

class Tela():
    def __init__(self):
        self.black = (0, 0, 0)
        self.clock = pygame.time.Clock()
    
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
        rect = Rect((300, 500), (400, 600))
        while True:
            self.texto(screen, name, (450, 380),self.black, 35)
            pygame.display.flip()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if event.key != pygame.K_SPACE:
                            c = pygame.key.name(event.key).upper()
                            if len(name) < 15:
                                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:-+_":
                                    name += c
                elif event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(mouse_pos):
                    return name