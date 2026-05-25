import funcoes
import time
import os

def humano_bot():
    M = funcoes.matriz10()
    A2 = [0,0,"◀","▩",0]
    
    A3 = [0,"◀","▩","▩",0]
    
    A4a = [0,"◀","▩","▩",0]
    A4b = [0,0,0,"▩",0]
    
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
                        x = funcoes.verif_cordenada_X()
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma2(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 2:
                    while verf == False:
                        x = funcoes.verif_cordenada_X()
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma3(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
                case 3:
                    while verf == False:
                        x = funcoes.verif_cordenada_X()
                        y = funcoes.verif_cordenada_Y()
                        verf = funcoes.colocar_arma4(M, x, y)
                        funcoes.showMatriz(M)
                    cont +=1
        else:
            print('Digite nova mente, houve um erro')
            continue
humano_bot()
