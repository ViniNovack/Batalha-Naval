import funcoes
import time
import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import funcoes_imagens
import funcoes

fu = funcoes
fi = funcoes_imagens



def humano_humano():

    mA = funcoes.matriz10()
    mB = funcoes.matriz10()


    #______________________________________________________ABERTURA________________________________________________
    time.sleep(1)
    fu.texto_star_wars('AGORA CADA UM ESCOLHA SEU LADO E JUNTOS DECIDEM O DESTINO DESSA HISTÓRIA\n')
    
    time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load('Audio_-Star-Wars-Epic.ogg') 
    pygame.mixer.music.play()
   
    fi.escudos_lado_a_lado()

    while True:
        try:
            opcao = int(input('» '))
            if opcao in range(1,3):
                pygame.mixer.music.stop()
                break
            else:
                print("Opção inválida, selecione novamente")
        except ValueError:
            print("Opção inválida, selecione novamente")

    if opcao == 1: #imperio
        os.system("cls")
        fu.texto_star_wars("Agora você é um comandante do Império Galático, erradique a escória rebelde.")
        fu.incluirNaves(mA)
        os.system("cls")
        fu.texto_star_wars("Os canhões de blaster já estão postos e apontados para nós, direcione as energias dos escudos para as armas e vamos nos defender.")
        fu.incluirNaves(mB)
        pass
    elif opcao == 2: #resistencia
        os.system("cls")
        fu.texto_star_wars("")
        fu.incluirNaves(mA)
        os.system("cls")
        fu.texto_star_wars("Os canhões de blaster já estão postos e apontados para nós, direcione as energias dos escudos para as armas e vamos nos defender.")
        fu.incluirNaves(mB)

        



if __name__ == '__main__':
    humano_humano()
