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
    M[x][y] = "◀"
    M[x][y + 1] = "▩"

def arma3():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,0,0]]

def arma4():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,"▩",0]]
    

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
    print()

def verif_cordenada_X():
    while True:
        x = int(input('Digite a cordenada X: '))
        if x == 1 or x == 2 or x == 3:
            break
        else:
            print('Resposta invalida, tente de novo')
    return x

def verif_cordenada_Y():
    while True:
        y = int(input('Digite a cordenada Y: '))
        if y == 1 or y == 2 or y == 3:
            break
        else:
            print('Resposta invalida, tente de novo')
    return y
