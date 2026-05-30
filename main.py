import time
import shutil
import os
import pygame
import funcoes_imagens

ff = funcoes_imagens

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
    #ff.texto()

    # for n in range(0, 36):
    #     time.sleep(1)
    #     print()

    os.system('cls')
    ff.centr('AGORA ESCOLHA UM LADO E DECIDA O DESTINO DESSA HISTÓRIA')
    time.sleep(1)



if __name__ == '__main__':
    main()
