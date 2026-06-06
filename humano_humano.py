import funcoes
import time
import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import funcoes_imagens
import funcoes

fu = funcoes
fi = funcoes_imagens



# EFEITOS SONOROS
# som_explosao = pygame.mixer.Sound("explosao.ogg")
# som_tiro = pygame.mixer.Sound("tiro.ogg")
# som_digitaçao = pygame.mixer.Sound("digitando.ogg")


class Cores:                              # Mensagemn de erro padrão: f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌'
    # VERMELHO
    vermelho = '\033[31m'
    # LIMPAR
    limpar = '\033[m'
c1 = Cores()



def humano_humano():

    mA = funcoes.matriz10()
    mB = funcoes.matriz10()
    vidaA = 0
    vidaB = 0
    mAAttack = fu.matriz10()
    mBAttack = fu.matriz10()

    
    #______________________________________________________ABERTURA________________________________________________
    time.sleep(1)
    # fu.texto_star_wars('AGORA CADA UM ESCOLHA SEU LADO E JUNTOS DECIDEM O DESTINO DESSA HISTÓRIA\n')
    
    # time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load('Audio_-Star-Wars-Epic.ogg') 
    pygame.mixer.music.play()

    fi.escudos_lado_a_lado()


    # -- MONTANDO AS MATRIZES ---------------------------------------

    while True:
        try:
            opcao = int(input('» '))
            if opcao in range(1,3):
                pygame.mixer.music.stop()
                break
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
        except ValueError:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')

    if opcao == 1: #imperio
        os.system("cls")
        # fu.texto_star_wars("Agora você é um comandante do Império Galático! Erradique a escória rebelde.")
        
        vidaA = fu.incluirNaves(mA)
        os.system("cls")
        # fu.texto_star_wars("Os canhões de blaster já estão postos e apontados para nós, direcione as energias dos escudos para as armas e vamos nos defender.")
        vidaB = fu.incluirNaves(mB)
        pass
    elif opcao == 2: #resistencia
        os.system("cls")
        # fu.texto_star_wars("")
        vidaA = fu.incluirNaves(mA)
        os.system("cls")
        # fu.texto_star_wars("Os canhões de blaster já estão postos e apontados para nós, direcione as energias dos escudos para as armas e vamos nos defender.")
        vidaB = fu.incluirNaves(mB)

    # ---------------------------------------------------------------

    

    # -- ATAQUES ----------------------------------------------------

    while (vidaA > 0 and vidaB > 0):
        fu.showFields(mAAttack,mBAttack, vidaA, vidaB)
        vidaA = fu.jogadasAtaque(mAAttack, mA, vidaA)
        fu.showFields(mAAttack,mBAttack, vidaA, vidaB)
        vidaB = fu.jogadasAtaque(mBAttack, mB, vidaB)


        
    



    



if __name__ == '__main__':
    humano_humano()
