import pygame
import time
import random 

pygame.init()

white = (255, 255, 255)
yelow = (255, 255, 102)
black = (0, 0, 0)
red = (253, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

largura_tela = 600
altura_tela = 400

tela = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Jogo da Cobrinha')

clock = pygame.time.Clock()

velocidade_cobrinha = 15

def nossa_cobrinha(tamanho_bloco, cobrinha_lista):
    for x in cobrinha_lista:
          pygame.draw.rect(tela, green, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def jogo():
     fim_de_jogo = False
     game_over = False
     pos_x_cobrinha = largura_tela/ 2
     pos_y_cobrinha = altura_tela/ 2
     velocidade_x = 0
     velocidade_y = 0
     cobrinha_lista = []
     comprimento_cobrinha = 1


     tamanho_bloco = 10


     while not fim_de_jogo:
          
          while game_over:
               tela.fill(blue)
               font = pygame.font.Sysfont("bahnschrift", 25)
               mensagem = font.render("Game Over! Pressione Q para Sair ou C para Jogar novamente", True, red)
               tela.blit(mensagem, [largura_tela/ 6, altura_tela/ 3])
               pygame.display.update()








#VAMOS FAZER UM JOGO DA COBRINHA MAS QUERO QUE ME EXPLIQUE TUDO,PRA CADA COISA QUE O CODIGO SERVE,ETAPA POR ETAPA E  ME DIGA QUE SERVE CADA CODIGO,SOU INICIANTE  E TO ESTUDANDO PYTHON E QUANDO EU FALAR VAMOS PARA O PROX PASSO

