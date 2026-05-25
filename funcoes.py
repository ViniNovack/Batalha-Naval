import random



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
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
        print("Resposta invalida, tente de novo")
        return False
    if y + 1 >= len(M[0]):
        print("Resposta invalida, tente de novo")
        return False
    if M[x][y] == "◀" or M[x][y] == "▩" or M[x][y + 1] == "◀" or M[x][y + 1] == "▩":
        print("Resposta invalida, tente de novo")
        return False
    M[x][y] = "◀"
    M[x][y + 1] = "▩"
    return True



def arma3():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,0,0]]



def colocar_arma3(M, x, y):
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
        print("Resposta invalida, tente de novo")
        return False
    if y + 2 >= len(M[0]):
        print("Resposta invalida, tente de novo")
        return False
    if M[x][y] == "◀" or M[x][y] == "▩" or M[x][y + 1] == "◀" or M[x][y + 1] == "▩" or M[x][y + 2] == "◀" or M[x][y + 2] == "▩":
        print("Resposta invalida, tente de novo")
        return False
    M[x][y] = "◀"
    M[x][y + 1] = "▩"
    M[x][y + 2] = "▩"
    return True



def arma4():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,"▩",0]]



def colocar_arma4(M, x, y):
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
        print("Resposta invalida, tente de novo")
        return False
    if y + 2 >= len(M[0]) or x + 1 >= len(M):
        print("Resposta invalida, tente de novo")
        return False
    if M[x][y] == "◀" or M[x][y] == "▩" or  M[x][y + 1] == "◀" or  M[x][y + 1] == "▩" or M[x][y + 2] == "◀" or M[x][y + 2] == "▩" or M[x + 1][y + 1] == "◀" or M[x + 1][y + 1] == "▩":
        print("Resposta invalida, tente de novo")
        return False
    M[x][y] = "◀"
    M[x][y + 1] = "▩"
    M[x][y + 2] = "▩"
    M[x + 1][y + 1] = "▩"
    return True  



def show_armas():
    grade2 = arma2()
    grade3 = arma3()
    grade4 = arma4()

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



def verif_cordenada_X():
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



def verif_cordenada_Y():
    while True:
        try:
            y = int(input('Digite a cordenada Y: '))
            if y in range(0, 10):
                return y
            else:
                print('Resposta invalida, tente de novo')
                continue
        except:
            print('Resposta invalida, tente de novo')
            continue
