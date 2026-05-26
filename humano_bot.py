import funcoes
import time
import os
import random

def humano_bot():
    MASC = funcoes.matriz10()
    M = funcoes.matriz10()
    A2 = [0,0,"◀","▩",0]
    
    A3 = [0,"◀","▩","▩",0]
    
    A4a = [0,"◀","▩","▩",0]
    A4b = [0,0,0,"▩",0]
    
    # HUMANO
    funcoes.showMatriz(M)
    cont = 0
    while cont <= 5:
        print("Escolha as naves que voce quer posicionar: ")
        print(' 1.', A2, '\n', '2.', A3, '\n', '3.', A4a, '\n', f'   {A4b}')
        try:
            n = int(input('Digite a númeração da nave: '))
        except:
            print('Digite nova mente, houve um erro')

        if n in range(1, 4):
            verf = False
            match n:
                case 1:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(1)
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma2(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 2:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(2)
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma3(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 3:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(3)
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma4(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
        else:
            print('Digite nova mente, houve um erro')
            continue
    
    # ROBO
    funcoes.showMatriz(M)
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
                        verf = funcoes.colocar_arma2(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 2:
                    while verf == False:
                        x = random.randrange(0, 9)
                        y = random.randrange(0, 9)
                        verf = funcoes.colocar_arma3(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 3:
                    while verf == False:
                        x = random.randrange(0, 9)
                        y = random.randrange(0, 9)
                        verf = funcoes.colocar_arma4(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
        else:
            print('Digite nova mente, houve um erro')
            continue
    
    # JOGO
    os.system('cls')
    print('O JOGO COMEÇOU'.center(30))
    for l in range(0, 10):
        for c in range(0, 10):
            print(f'[{MASC[l][c]}]', end='')
        print()

humano_bot()
