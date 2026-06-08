import time
import shutil
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import funcoes_imagens
import funcoes
import humano_bot
import humano_humano


fi = funcoes_imagens
fu = funcoes


def final_rebeldes_vencedores():
    os.system('cls')
    pygame.mixer.init()
    pygame.mixer.music.load('22-Ben-Kenobi_s-Death-Tie-Fighter-Attack.ogg')
    pygame.mixer.music.play()
    fu.texto_star_wars('...')
    time.sleep(3)
    os.system('cls')
    fu.masc_imperio(4)




    pygame.mixer.music.stop()
    fi.imagem_fim()


if __name__ == '__main__':
    final_rebeldes_vencedores()
