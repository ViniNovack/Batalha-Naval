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


def final_imperio_vencedor():
    os.system('cls')
    fu.texto_star_wars('...')
    time.sleep(3)
    os.system('cls')
    fu.masc_resistencia(4)
    fu.texto_star_wars('Foi um prazer conhecer todos vocês')
    fu.texto_star_wars('Me orgulho de ter dado mais tempo de esperança para um planeta…')
    time.sleep(2.5)
    os.system('cls')
    fu.texto_star_wars_sem_musica('Que a força estej')
    time.sleep(0.5)
    os.system('cls')
    fi.esploção_das_naves()
    time.sleep(1)
    os.system('cls')
    pygame.mixer.init()
    pygame.mixer.music.load('Star-Wars-Imperial-March.ogg')
    pygame.mixer.music.play()
    fu.texto_star_wars_sem_musica('Generais!!')
    fu.texto_star_wars_sem_musica('Hoje conseguimos livrar a galáxia de mais inimigos do Império!')
    time.sleep(3)
    os.system('cls')
    fu.texto_star_wars_sem_musica('Comandante!')
    fu.texto_star_wars_sem_musica('Me desculpe, mas teve uma nave que atracou no nosso hangar')
    time.sleep(3)
    os.system('cls')
    fu.texto_star_wars_sem_musica('De quem é essa nave?')
    fu.texto_star_wars_sem_musica('É do Lord …')
    time.sleep(0.5)
    os.system('cls')
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load('respiração.ogg')
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
    fi.imagem_fim()


if __name__ == '__main__':
    final_imperio_vencedor()
