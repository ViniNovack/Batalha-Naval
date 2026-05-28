import funcoes
import time
import os
import random

def humano_bot():
    MASCH = funcoes.matriz10()
    MASCR = funcoes.matriz10()
    MH = funcoes.matriz10()
    MR = funcoes.matriz10()

    vidaR = 0
    vidaH = 0
    
    A2 = [0,0,"◀","▩",0]
    
    A3 = [0,"◀","▩","▩",0]
    
    A4a = [0,"◀","▩","▩",0]
    A4b = [0,0,0,"▩",0]
    
    # HUMANO
    funcoes.showMatriz(MH)
    cont = 0
    while cont <= 5:
        print("Escolha as naves que voce quer posicionar: ")
        print(' 1.', A2, '\n', '2.', A3, '\n', '3.', A4a, '\n', f'   {A4b}')
        try:
            n = int(input('Digite a númeração da nave: '))
        except:
            print('Digite nova mente, houve um erro')
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
                    cont +=1
                    vidaH += 2
                case 2:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(2)
                        y = funcoes.verif_cordenada_Y(0)
                        verf = funcoes.colocar_arma3(MH, x, y)
                        funcoes.showMatriz(MH)
                    cont +=1
                    vidaH += 3
                case 3:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(3)
                        y = funcoes.verif_cordenada_Y(1)
                        verf = funcoes.colocar_arma4(MH, x, y)
                        funcoes.showMatriz(MH)
                    cont +=1
                    vidaH +=4
        else:
            print('Digite nova mente, houve um erro')
            continue
    
    # ROBO
    funcoes.showMatriz(MR)
    cont = 0
    while cont <= 5:
        print("Escolha as naves que voce quer posicionar: ")
        print(' 1.', A2, '\n', '2.', A3, '\n', '3.', A4a, '\n', f'   {A4b}')
        try:
            print('Digite a númeração da nave: ', end='')
            n = random.randrange(1, 4)
            print(n)
        except:
            print('Digite nova mente, houve um erro')
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
            print('Digite nova mente, houve um erro')
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

humano_bot()
