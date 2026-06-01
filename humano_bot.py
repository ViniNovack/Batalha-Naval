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
    MH = funcoes.matriz10()
    MR = funcoes.matriz10()

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
        funcoes.showMatriz(MH)
        cont = 0
        print()
        fu.texto_star_wars_sem_musica("Você tem 3 opções de armas para posicionar estrategicamente para ELIMINAR os rebeldes invasores… PERMANENTEMENTE ")
        time.sleep(1.5)

        while cont <= 5:
            os.system('cls')
            print("-"*45)
            funcoes.show_armas()
            print("-"*45)
            print("\nobs.: Você deverá posicionar pela ponta delas: ◀")

            try:
                n = int(input('Digite a númeração da nave: '))
            except:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                time.sleep(0.5)
                continue

            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        while verf == False:
                            x = funcoes.verif_cordenada_X(1)
                            y = funcoes.verif_cordenada_Y(0)
                            verf = funcoes.colocar_arma2(MH, x, y)
                            funcoes.showMatriz(MH)
                            time.sleep(0.5)
                        cont +=1
                        vidaH += 2
                    case 2:
                        while verf == False:
                            x = funcoes.verif_cordenada_X(2)
                            y = funcoes.verif_cordenada_Y(0)
                            verf = funcoes.colocar_arma3(MH, x, y)
                            funcoes.showMatriz(MH)
                            time.sleep(0.5)
                        cont +=1
                        vidaH += 3
                    case 3:
                        while verf == False:
                            x = funcoes.verif_cordenada_X(3)
                            y = funcoes.verif_cordenada_Y(1)
                            verf = funcoes.colocar_arma4(MH, x, y)
                            funcoes.showMatriz(MH)
                            time.sleep(0.5)
                        cont +=1
                        vidaH +=4
                time.sleep(0.5)
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                time.sleep(0.5)
                continue
        
        # ROBO
        funcoes.showMatriz(MR)
        cont = 0
        while cont <= 5:
            try:
                print('Digite a númeração da nave: ', end='')
                n = random.randrange(1, 4)
                print(n)
            except:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        while verf == False:
                            x = random.randrange(0, 9)
                            y = random.randrange(0, 9)
                            verf = funcoes.colocar_arma2(MR, x, y)
                            funcoes.showMatriz(MR)
                        cont +=1
                        vidaR +=2
                    case 2:
                        while verf == False:
                            x = random.randrange(0, 9)
                            y = random.randrange(0, 9)
                            verf = funcoes.colocar_arma3(MR, x, y)
                            funcoes.showMatriz(MR)
                        cont +=1
                        vidaR +=3
                    case 3:
                        while verf == False:
                            x = random.randrange(0, 9)
                            y = random.randrange(0, 9)
                            verf = funcoes.colocar_arma4(MR, x, y)
                            funcoes.showMatriz(MR)
                        cont +=1
                        vida +=4
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                continue
        
        # JOGO
        os.system('cls')
        print('O JOGO COMEÇOU'.center(30))
        print()
        resul = False

        while vidaH != 0 or vidaR != 0:
            os.system('cls')
            print('Espaço da Resistencia'.center(10))
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
            resul = funcoes.jogadas_ataque(MR, x, y, MASCR)
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
            resul = funcoes.jogadas_ataque(MH, x, y, MASCH)
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
