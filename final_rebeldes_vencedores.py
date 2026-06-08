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
    fu.texto_star_wars_sem_musica('...')
    time.sleep(3)
    os.system('cls')
    fu.masc_imperio(4)
    fu.texto_star_wars_sem_musica('Senhor…')
    fu.texto_star_wars_sem_musica('Eles escaparam')
    time.sleep(3)
    os.system('cls')
    fi.esploção_das_naves()
    fu.texto_star_wars_sem_musica('O bloqueio estelar foi furado')
    time.sleep(3)
    os.system('cls')
    fu.texto_star_wars_sem_musica('Não… Não…')
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
    os.system('cls')
    pygame.mixer.init()
    pygame.mixer.music.load('Audio_-Star-Wars-Epic.ogg')
    pygame.mixer.music.play()
    fu.texto_star_wars_sem_musica('Conseguimos!!!')
    fu.texto_star_wars_sem_musica('Estamos vivos!!!')
    time.sleep(2)
    os.system('cls')
    fi.imagem_nave_indo_em_bora()
    time.sleep(3)
    fu.texto_star_wars_sem_musica('Ative os propulsores, vamos entrar no hiperespaço')
    fu.texto_star_wars_sem_musica('Estamos voltando para a base!!!')
    time.sleep(4)
    os.system('cls')
    pygame.mixer.music.stop()
    fi.imagem_fim()


if __name__ == '__main__':
    final_rebeldes_vencedores()
