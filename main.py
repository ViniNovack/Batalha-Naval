import time
import shutil
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import funcoes_imagens
import funcoes
import humano_bot
import humano_humano


ff = funcoes_imagens
fu = funcoes

def main():
    pygame.mixer.init()
    pygame.mixer.music.load('Star-Wars-Main-Theme-_Full_.ogg') 
    pygame.mixer.music.play()
    
    ff.episodio()
    time.sleep(2)
    os.system('cls')

    time.sleep(2)
    ff.titulo()
       
    time.sleep(1)
    ff.texto()

    for n in range(0, 36):
        time.sleep(1)
        print()

    os.system('cls')
    ff.centr('PARA CONTINUAR ESSA HISTÓRIA, ESCOLHA UMA OPÇÃO DE JOGO\n')
    time.sleep(1)
    
    ff.centr('  ___MENU___  ')
    ff.centr('1. HUMANO X BOT')
    ff.centr('2. HUMANO X HUMANO')
    x = fu.verif_int('Digite sua opção de jogo: ', 3)
    pygame.mixer.music.stop()
    if x == 1:
        os.system('cls')
        humano_bot.humano_bot()
    elif x == 2:
        os.system('cls')
        humano_humano.humano_humano()



if __name__ == '__main__':
    main()
