import random
import shutil
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def matriz10():
    return [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]



def arma2():
    return [[0,0,0,0,0],
            [0,0,"◀","▩",0],
            [0,0,0,0,0]]



def colocar_arma2(M, x, y):
    if (M[y][x] != 0 or M[y][x + 1] != 0):
        print("A arma não pode sobrepor outra, tente de novo")
        return False
    
    M[y][x] = "◀"
    M[y][x + 1] = "▩"
    return True



def arma3():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,0,0]]



def colocar_arma3(M, x, y):
    if (M[y][x] !=0 or M[y][x + 1] != 0 or M[y][x + 2] != 0):
        print("A arma não pode sobrepor outra, tente de novo")
        return False
    
    M[y][x] = "◀"
    M[y][x + 1] = "▩"
    M[y][x + 2] = "▩"
    return True



def arma4():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,"▩",0]]



def colocar_arma4(M, x, y):
    if (M[y][x] != 0 or M[y][x + 1] != 0 or M[y][x + 2] !=0 or M[y + 1][x + 1] != 0):
        print("A arma não pode sobrepor outra, tente de novo")
        return False
    
    M[y][x] = "◀"
    M[y][x + 1] = "▩"
    M[y][x + 2] = "▩"
    M[y + 1][x + 1] = "▩"
    return True  



def show_armas():
    grade2 = arma2()
    grade3 = arma3()
    grade4 = arma4()

    print("1." + " "*15 + "2." + " "*15 + "3." + " "*15)

    for i in range(3): 
        print(*grade2[i], end = "")
        print("        ", end = "")
        print(*grade3[i], end = "")
        print("        ", end = "")
        print(*grade4[i], end = "")
        print()



def showMatriz(matriz):
    print()

    print("    ", end = "")
    
    for linha in range(len(matriz[0])):
            print(linha, end=" ")

    print()
    print("   ", end = "")
    print("—⊽"*len(matriz[0]) + "—")

    x = 0
    for i in matriz:
        print(f"{x} ⊳ ", end = "")
        print(*i)
        x +=1



def verif_cordenada_X(size):
    while True:
        try:
            x = int(input('Digite a cordenada X: '))
            if x in range(0, 10):
                if x+size in range(0, 10):
                    return x
                else:
                    print('Resposta invalida, tente de novo')
                    continue
            else:
                print('Resposta invalida, tente de novo')
                continue
        except:
            print('Resposta invalida, tente de novo')
            continue
                    


def verif_cordenada_XX():
    while True:
        try:
            x = int(input('Digite a cordenada X: '))
            if x in range(0, 10):
                return x
            else:
                print('Resposta invalida, tente de novo')
                continue
        except:
            print('Resposta invalida, tente de novo')
            continue



def verif_cordenada_Y(size):
    while True:
        try:
            y = int(input('Digite a cordenada Y: '))
            if y in range(0, 10):
                if y+size in range (0,10):
                    return y
                else:
                    print('Resposta invalida, tente de novo')
                    continue
            else:
                print('Resposta invalida, tente de novo')
                continue
        except:
            print('Resposta invalida, tente de novo')
            continue

def incluirNaves(m):
        showMatriz(m)
        print("\nEssas são suas opcções de canhão:")
    
        cont = 0

        while cont < 5:
            print("-"*45)
            show_armas()
            print("-"*45)
            print(f"Prepare seu campo de batalha selecionando e posicionando 5 canhões")
            print("\nobs.: Você deverá posicionar pela ponta delas: ◀")

            try:
                n = int(input('Digite a númeração do canhão: '))
            except:
                print('Digite nova mente, houve um erro')
                continue

            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        while verf == False:
                            x = verif_cordenada_X(1)
                            y = verif_cordenada_Y(0)
                            verf = colocar_arma2(m, x, y)
                            showMatriz(m)
                        cont +=1
                        
                    case 2:
                        while verf == False:
                            x = verif_cordenada_X(2)
                            y = verif_cordenada_Y(0)
                            verf = colocar_arma3(m, x, y)
                            showMatriz(m)
                        cont +=1
                        
                    case 3:
                        while verf == False:
                            x = verif_cordenada_X(3)
                            y = verif_cordenada_Y(1)
                            verf = colocar_arma4(m, x, y)
                            showMatriz(m)
                        cont +=1
                        
            else:
                print('Digite nova mente, houve um erro')
                continue



def jogadas_ataque(M, x, y, MM=0):
    if M[x][y] == "◀" or M[x][y] == "▩":
        M[x][y] = '💥'
        MM[x][y] = '💥'
        return True
    else:
        M[x][y] = '🌟'
        MM[x][y] = '🌟'
        return False



def masc(M):
    for l in range(0, 10):
        for c in range(0, 10):
            print(f'[{M[l][c]}]', end='')
        print()



def centr(texto):
    largura_terminal = shutil.get_terminal_size().columns
    linha_centralizada = texto.center(largura_terminal)
    print(linha_centralizada)



def verif_int(texto, n:int=0):
    while True:
        try:
            x = int(input(f'{texto}'))
            if x in range(1, n):
                return x
            else:
                print('Resposta invalida!!, tente de novo')
                continue
        except:
            print('Resposta invalida!!, tente de novo')
            continue



def texto_star_wars(texto, nud=11, nur=61):
    pygame.mixer.init()
    pygame.mixer.music.load('digitando.ogg')

    largura_terminal = shutil.get_terminal_size().columns
    linha_centralizada = texto.center(largura_terminal)
    x = 1
    y = 0
    pygame.mixer.music.play(-1)
    for c in linha_centralizada:
        if c == ' ':
            print(c, end='', flush=True)
        else:
            if x == 1:
                print(c,end='', flush=True)
                time.sleep(0.2)
                y +=1
                if y == nud:
                    y = 0
                    x = 2
            elif x == 2:
                print(c,end='', flush=True)
                time.sleep(0.02)
                y +=1
                if y == nur:
                    y = 0
                    x = 1
    pygame.mixer.music.stop()
    print()



if __name__ == '__main__':
    pass
