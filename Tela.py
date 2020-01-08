import pygame 
from pygame.locals import *
from sys import exit

class Tela():
    def __init__(self):
        self.black = (0, 0, 0)
        self.yellow = (255, 255, 0)
        self.tam = (1000, 680)
    
    def criaTela(self, nameScreen):
        img = pygame.image.load("%s.png"%nameScreen)
        w, h = img.get_size()
        redImg = pygame.transform.smoothscale(img, (int(w*0.80), int(h*0.80)))
        
        tela = pygame.display.set_mode(self.tam, 0, 32)
        tela.fill((255,255,255))
        pygame.display.set_caption("QUIZ_PY")
               
        tela.blit(redImg, (0, 0))
        pygame.display.flip()
        return tela
    
    def texto(self, tela, mensagem, posicao, cor, tam):
        arial = pygame.font.SysFont('arial', tam)
        mens = arial.render(mensagem, True, cor, 0)
        tela.blit(mens, posicao)
        
    def getName(self, screen):
        name = ""
        rect = Rect((280, 380), (750, 450))
        while True:
            self.texto(screen, name, (350, 280),self.black, 35)
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
                
    def test(self, namePlayer):
        tela = pygame.display.set_mode((400, 400), 0, 32)
        pygame.display.set_caption("QUIZ_PY")
        tela.fill(self.yellow)
        
        self.texto(tela, "%s!"%namePlayer, (100, 100), self.black, 20)
        self.texto(tela, "AGUADE CONEXAO...", (100, 200), self.black, 20)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        return tela
    
    def getOpcoes(self, screen):
        """
        a = (50, 280) (410, 330)
        b = (50, 440) (410, 500)
        c = (610, 280) (960, 330)
        d = (610, 440) (960, 500)
        p = ()
        n = ()
        """
        #self.texto(screen, ".", (410, 330),self.black, 35)
        #pygame.display.flip()
        #Falta pergunta e numero
        a = Rect((50, 280), (360, 80))
        b = Rect((50, 440), (360, 80))
        c = Rect((610, 280), (360, 80))
        d = Rect((610, 440), (360, 80))
        
        return self.testa_pos([a, b, c, d])
        
    def testa_pos(self, rec):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                for p in rec:
                    if event.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
                        if p == rec[0]:
                            print("A")
                        if p == rec[1]:
                            print("B")
                        if p == rec[2]:
                            print("C")
                        if p == rec[3]:
                            print("D")
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
