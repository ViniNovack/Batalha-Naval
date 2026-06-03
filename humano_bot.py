import funcoes
import time
import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import random
import funcoes_imagens
import funcoes


fu = funcoes
fi = funcoes_imagens

class Cores:                              # Mensagemn de erro padrão: f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌'
    # VERMELHO
    vermelho = '\033[31m'
    # LIMPAR
    limpar = '\033[m'
c1 = Cores()



def humano_bot():
    MASCH = funcoes.matriz10()
    MASCR = funcoes.matriz10()
    mH = funcoes.matriz10()
    mR = funcoes.matriz10()

    vidaR = 0
    vidaH = 0
#______________________________________________________ABERTURA________________________________________________
    time.sleep(1)
    fu.texto_star_wars('AGORA ESCOLHA UM LADO E DECIDA O DESTINO DESSA HISTÓRIA\n')
    
    time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load('Audio_-Star-Wars-Epic.ogg') 
    pygame.mixer.music.play()
   
    fi.escudos_lado_a_lado()
    opcao = fu.verif_int('» ', 3)
    pygame.mixer.music.stop()

    if opcao == 1:
        os.system('cls')
        pygame.mixer.init()
        pygame.mixer.music.load('Star-Wars-Imperial-March.ogg') 
        pygame.mixer.music.play(-1)
        fu.texto_star_wars_sem_musica("Você decidiu ser um comandante do grande e poderoso Império Galático")
        fu.texto_star_wars_sem_musica("Assuma seu posto e extermine essa escória rebelde")
        time.sleep(3)
        os.system('cls')

        #_____________________________________________JOGO____________________________________________

        # HUMANO
        cont = 0
        print()
        fu.texto_star_wars_sem_musica("Você deve posicionar estrategicamente 5 armas para ELIMINAR os rebeldes invasores… PERMANENTEMENTE ")
        time.sleep(2.5)

        vidaH = fu.incluirNaves(mH)
        
        os.system('cls')
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load('Star-Wars-Imperial-March.ogg') 
        pygame.mixer.music.play(-1)
        fu.texto_star_wars_sem_musica('Agora, com todos os canhões posicionados, podemos começar a atacar')
        fu.texto_star_wars_sem_musica('Precisamos impedir que eles passem o bloqueio e entrem no hiperespaço')
        time.sleep(2)
        os.system('cls')
        fu.texto_star_wars_sem_musica('“General!! Ligue o monitor da nave e vamos começar o ataque”')
        fu.texto_star_wars_sem_musica('"Isso foi uma ORDEM!!"')
        time.sleep(2)
        os.system('cls')
        fu.masc_imperio(1)
        time.sleep(3)
        pygame.mixer.music.stop()
        
        # ROBO
        os.system('cls')
        fu.texto_star_wars('REBELDES!!!')
        pygame.mixer.init()
        pygame.mixer.music.load('March-of-the-Resistance.ogg') 
        pygame.mixer.music.play(-1)
        time.sleep(2)
        os.system('cls')
        fu.texto_star_wars_sem_musica('Estamos sob fogo pesado de um destróier!!!')
        fu.texto_star_wars_sem_musica('Precisamos ganhar tempo para escapar do bloqueio estelar e entrar no hiperespaço')
        time.sleep(2.5)
        os.system('cls')
        fu.texto_star_wars_sem_musica('Redirecionem a energia dos escudos para os canhões e para os motores')
        fu.texto_star_wars_sem_musica('E mirem as armas para o destróier')
        time.sleep(2.5)
        os.system('cls')
        fu.texto_star_wars_sem_musica('PRECISAMOS CONTRA-ATACAR!!!')
        time.sleep(2.5)
        os.system('cls')
        fi.dentro_da_nave_resistencia()
        cont = 0
        while cont < 5:
            n = random.randrange(1, 4)
 
            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        while verf == False:
                            x = random.randrange(0, 9) 
                            y = random.randrange(0, 10)

                            verf = funcoes.colocar_arma2(mR, x, y, False)
                        cont +=1
                        vidaR +=2
                    case 2:
                        while verf == False:
                            x = random.randrange(0, 8)
                            y = random.randrange(0, 10)
                            verf = funcoes.colocar_arma3(mR, x, y, False)
                        cont +=1
                        vidaR +=3
                    case 3:
                        while verf == False:
                            x = random.randrange(0, 8)
                            y = random.randrange(0, 9)
                            verf = funcoes.colocar_arma4(mR, x, y, False)
                        cont +=1
                        vidaR +=4
            else:
                continue
    
        time.sleep(3)
        os.system('cls')
        fu.texto_star_wars_sem_musica('“Tudo pronto!!! Armas apostas e energia redirecionada”')
        time.sleep(3)
        os.system('cls')
        fu.masc_resistencia(1)
        time.sleep(3)
        os.system('cls')
        fu.texto_star_wars_sem_musica('VAMOS FUGIR DAQUI !!!')
        time.sleep(2.5)
        pygame.mixer.music.stop()
        os.system('cls')


        # JOGO
        fi.imagem_texto_batalha()
        time.sleep(2.5)
        os.system('cls')

        resul = False
        while vidaH != 0 or vidaR != 0:
            os.system('cls')
            
            funcoes.masc(MASCH)
            print()
            print('Espaço do Imperio'.center(10))
            funcoes.masc(MASCR)
            print()
            
            # JOGADAS
            os.system('cls')
            print('Faça seu ataque')
            x = funcoes.verif_cordenada_XX()
            y = funcoes.verif_cordenada_Y()
            resul = funcoes.jogadas_ataque(mR, x, y, MASCR)
            funcoes.masc(MASCR)
            if resul == True:
                print('Você ACERTOU')
                vidaR -=1
            else:
                print('Você ERROU')

            os.system('cls')
            print('Minha vez')
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
            resul = funcoes.jogadas_ataque(mH, x, y, MASCH)
            funcoes.masc(MASCH)
            if resul == True:
                print('Eu ACERTEI')
                vidaH -=1
            else:
                print('EU ERREI')
        
        # FIM
        if vidaH == 0:
            print('VOCÊ DEIXOU O IMPERIO VENCER')
        else:
            print('PARABENS VOCE DESTRUIU COM OS PLANOS DO IMPARIO')

    
    



    elif opcao == 2:
        pass















if __name__ == '__main__':
    humano_bot()
