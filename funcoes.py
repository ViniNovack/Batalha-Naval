import random
import shutil
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame



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



def colocar_arma2(M, x, y, f:float=True):
    if (M[y][x] != 0 or M[y][x + 1] != 0):
        if f == True:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
        return False
    
    M[y][x] = "◀"
    M[y][x + 1] = "▩"
    return True



def arma3():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,0,0,0]]



def colocar_arma3(M, x, y, f:float=True):
    if (M[y][x] !=0 or M[y][x + 1] != 0 or M[y][x + 2] != 0):
        if f == True:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
        return False
    
    M[y][x] = "◀"
    M[y][x + 1] = "▩"
    M[y][x + 2] = "▩"
    return True



def arma4():
    return [[0,0,0,0,0],
            [0,"◀","▩","▩",0],
            [0,0,"▩",0,0]]



def colocar_arma4(M, x, y, f:float=True):
    if (M[y][x] != 0 or M[y][x + 1] != 0 or M[y][x + 2] !=0 or M[y + 1][x + 1] != 0):
        if f == True:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
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
    print('▾▾▾▾▾▾▾▾▾', end='')
    print('        ', end='')
    print('▾▾▾▾▾▾▾▾▾', end='')
    print('        ', end='')
    print('▾▾▾▾▾▾▾▾▾', end='')
    print()

    print('Vida +=2', end='')
    print("         ", end = "")
    print('Vida +=3', end='')
    print("         ", end = "")
    print('Vida +=4')



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

def showField(m,vida):
    print()

    print("    ", end = "")
    
    for linha in range(len(m[0])):
            print(linha, end=" ")

    print()
    print("   ", end = "")
    print("—⊽"*len(m[0]) + "—")

    x = 0
    for i in m:
        print(f"{x} ⊳ ", end = "")
        print(*i)
        x +=1

    # -- mostra a vida ----------
    print()

    print(f"Vida: {vida}", end="")

    
    # ---------------------------


def showFields(ma,mb, vidaA, vidaB):

    # -- mostra o titulo ----------

    print(" "*10, end = "") # recuo
    print(f"IMPERIO", end="")

    print(" "*25, end="") #espaço do meio

    print(f"RESISTENCIA")

    # ---------------------------

    print()

    # -- mostra matrizes com coordenadas --

    print(" "*4, end = "")
    
    for coluna in range(10):
        print(coluna, end=" ")

    print(" "*10, end="") #espaço do meio
    print(" "*3, end = "") # recuo


    for coluna in range(10):
        print(coluna, end=" ")

    print()
    print(" "*3, end = "") # recuo
    print("—⊽"*10 + "—", end="")

    print(" "*10, end="") #espaço do meio
    print(" "*2, end = "") # recuo

    print("—⊽"*10 + "—")



    for i in range(10):
        print(f"{i} ⊳ ", end = "")
        print(*ma[i], end = "")
        print(" "*10, end="") #espaço do meio
        print(f"{i} ⊳ ", end = "")
        print(*mb[i])

    # ---------------------------

    # -- mostra a vida ----------
    print()

    print(f"Vida: {vidaA}", end="")

    print(" "*25, end="") #espaço do meio

    print(f"Vida: {vidaB}")

    # ---------------------------



def verif_cordenada_X(size):
    while True:
        try:
            x = int(input('Digite a coluna: '))
            if x in range(0, 10):
                if x+size in range(0, 10):
                    return x
                else:
                    print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                    continue
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                continue
        except:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
            continue



def verif_cordenada(sentido):
    while True:
        try:
            x = int(input(f'Digite a {sentido}: '))
            if x in range(0, 10):
                return x
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                continue
        except:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
            continue



def verif_cordenada_Y(size):
    while True:
        try:
            y = int(input('Digite a linha: '))
            if y in range(0, 10):
                if y+size in range (0,10):
                    return y
                else:
                    print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                    continue
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                continue
        except:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
            continue



def incluirNaves(m):
        vida = 0
        while vida != 15:
            centr("\nPosicione os canhões até que some 15 de vida, escolha sabiamente.")
            showMatriz(m)
            print("\nEssas são suas opções de canhões:")
            print("-"*45)
            show_armas()
            print("-"*45)
            print("\nobs.: Você deverá posicionar pela ponta delas: ◀")
            print(f'\nVida atual = {vida}')
            
            try:
                n = int(input('Digite a númeração do canhão: '))
            except:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                time.sleep(1)
                os.system("cls")
                continue
            
            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        if(vida == 12 or vida ==14):
                            print(f'❌{c1.vermelho}Sua vida ultrapasará 15, escolha outro canhão.{c1.limpar}❌')
                            time.sleep(1)
                        else:
                            while verf == False:
                                x = verif_cordenada_X(1)
                                y = verif_cordenada_Y(0)
                                verf = colocar_arma2(m, x, y)
                            vida += 2
                    case 2:
                        if(vida == 14 or vida == 13 or vida == 11):
                            print(f'❌{c1.vermelho}Sua vida ultrapasará 15, escolha outro canhão.{c1.limpar}❌')
                            time.sleep(1)
                        else:
                            while verf == False:
                                x = verif_cordenada_X(2)
                                y = verif_cordenada_Y(0)
                                verf = colocar_arma3(m, x, y)
                            vida += 3
                    case 3:
                        if(vida == 14 or vida == 13 or vida == 12 or vida == 10):
                            print(f'❌{c1.vermelho}Sua vida ultrapasará 15, escolha outro canhão.{c1.limpar}❌')
                            time.sleep(1)
                        else:
                            while verf == False:
                                x = verif_cordenada_X(2)
                                y = verif_cordenada_Y(1)
                                verf = colocar_arma4(m, x, y)
                            vida += 4
                os.system("cls")      
            else:
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                time.sleep(1)
                os.system("cls")
                continue
        return vida



def atacar(x,y, m, mAttack):
    if(m[y][x] != 0):
        pygame.mixer.music.pause()
        som_explosao = pygame.mixer.Sound("explosao.ogg")
        som_explosao.set_volume(1)
        som_explosao.play()
        time.sleep(4)
        pygame.mixer.music.unpause()

        mAttack[y][x] = 'X'
        return True
    else:

        mAttack[y][x] = '#'
        return False



def jogadasAtaque(mAttack, m, vida, lado):
    while True:
        try:
            x = verif_cordenada('coluna')
            y = verif_cordenada('linha')
            if(mAttack[y][x] != 0):
                print(f'❌{c1.vermelho} Você já tentou aí! É ASSIM QUE QUER VENCER? {c1.limpar}❌')
            else:
                os.system("cls")
                pygame.mixer.init()
                pygame.mixer.Sound("tiro.ogg").play()
                time.sleep(1)
                if (atacar(x,y,m,mAttack)):
                    vida -= 1
                    if lado == 'r':
                        texto_star_wars(falas_do_imperio(2))
                    else:
                        texto_star_wars(falas_da_resistencia(2))
                else:
                    if lado == 'r':
                        texto_star_wars(falas_do_imperio(1))
                    else:
                        texto_star_wars(falas_da_resistencia(1))
                return vida
            
        except ValueError:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')



def falas_do_imperio(parametro):
    y = ''
    if parametro == 1:     #QUANDO ERRAR
        x = random.randrange(1, 4)
        match x:
            case 1:
                y = 'Tiro perdido. Inaceitável. O Império exige perfeição.'
            case 2:
                y = 'Os rebeldes são escorregadios… mas a sorte deles tem um fim.'
            case 3:
                y = 'Ajustem as miras! Não desperdicem munição imperial!'
        return y
    elif parametro == 2:   #QUANDO ACERTAR
        x = random.randrange(1, 5)
        match x:
            case 1:
                y = 'Impacto confirmado. Mais um fragmento da nave foi destruído. '
            case 2:
                y = 'Os rebeldes pagam o preço de desafiar o Imperador.'
            case 3:
                y = 'Fogo certeiro! A galáxia logo voltará à ordem imperial.'
            case 4:
                y = 'O Império não tolera rebeldes!!'
        return y



def falas_da_resistencia(parametro):
    y = ''
    if parametro == 1:     #QUANDO ERRAR
        x = random.randrange(1, 4)
        match x:
            case 1:
                y = 'Errou! As interferências imperiais estão nos cegando!'
            case 2:
                y = 'Nada! O Império tem escudos de interferência… mas nós vamos contornar isso.'
            case 3:
                y = 'Os sensores estão com falha. Ajustem as frequências!'
    elif parametro == 2:   #QUANDO ACERTAR
        x = random.randrange(1, 5)
        match x:
            case 1:
                y = 'Impacto direto! Os sistemas imperiais começam a falhar!'
            case 2:
                y = 'Atingido! O sinal do inimigo está ficando mais claro para os nossos sensores!'
            case 3:
                y = 'Boa mira, soldado! Estou sentindo a esperança crescer!'
            case 4:
                y = 'Escudo imperial comprometido! Continuem atirando!'
    return y



def jogadas_ataque(m, mAt, x, y, parametro):
    pygame.mixer.init()
    pygame.mixer.Sound("tiro.ogg").play()
    time.sleep(1)
    if parametro == 1:              #IMPERIO
        if m[x][y] == "◀" or m[x][y] == "▩":
            pygame.mixer.music.pause()
            som_explosao = pygame.mixer.Sound("explosao.ogg")
            som_explosao.set_volume(1)
            som_explosao.play()
            mAt[x][y] = 'X'
            texto_star_wars(falas_do_imperio(2))
            time.sleep(4)
            pygame.mixer.music.unpause()
            return True
        else:
            mAt[x][y] = '#'
            texto_star_wars(falas_do_imperio(1))
            return False
    elif parametro == 2:            #RESISTENCIA
        if m[x][y] == "◀" or m[x][y] == "▩":
            pygame.mixer.music.pause()
            som_explosao = pygame.mixer.Sound("explosao.ogg")
            som_explosao.set_volume(1)
            som_explosao.play()
            mAt[x][y] = 'X'
            texto_star_wars(falas_da_resistencia(2))
            time.sleep(4)
            pygame.mixer.music.unpause()
            return True
        else:
            mAt[x][y] = '#'
            texto_star_wars(falas_da_resistencia(1))
            return False



def masc_imperio(s):
    match s:
        case 1:
            nave = """
                                                                                                                                        
                                                                                                 .....                  
                                                                                               .'::;;;.                 
                                                                                              ':;,;;;;.                 
                                                                                           .';;;,,,,;:.                 
                                                                                          ';:;;,,,,,;;.                 
                                                                                       .';:;,,,,,,,,;:.                 
                                                     ....',:::;,...                  .'::;;;;;;;;;;;:;.                 
                                          ....''',;:::clllllllllccc:;,'...     ...',;ccllllloollollc;'.....             
                                        .;cccllccclllllllcclllloc:clllccc:;'',;ccllllllooolooloooolc;;;;::;.            
                      ....''',;::;,'',;:cccllooocclololc:c:::clolcclolllllllcccllllccllllccloooooooc;;;:::;.            
            ....''',;:cccllllllllllllllllloooooolclllol:cllc;cllc:clolccclolccclllccclllcccllllooolc:,',,,'...',,'..    
     .''',;:::clllllllllllooooooooooooooolooloolllcloolc:::::clolclooollllcllcclccccllllllllcccllooll:,;;;,,,,:::::.    
   .:clllllllloooooooooooooooooooooooooollllllllcccccllllcllccllollllclllcccllllllllllllllllcclccllcc:;:::;'...''..     
  .,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'''''''''''''''''''''',:cccccccccccccloollllllllcllllcllc:cccccllllcc:ccc::,.  
  .'............................................................,clllllllllllcclollllllllllllllllcclllllccllllllccccc.  
  .,'''''''''''''''''''''''''''''''''''........................';cccccllcclccccllllllllllllllllllcccllccclllllllllllc.  
  .,:ccccccccccccccccccclccccccccccccccc:;;;;;;;;;;;;;;;;;;;;;;:clllccccccccclloollllllllcclclllccccccccccc;,',,,,'..   
    .,::cccllcllllllooooolooollooooololoooooooooollclooolcclloollllolllllc:clclcccccllllllllcclccloll:;;;;,...',,,'.    
       ....''',;:::clllllllllllooollllloolollooolccloolc:::::cllc:clollcllllcccllcccllllcccllcllloolc;,,,,',,,;:::;.    
                  ...''',;:::clllc::cclllllooloolclolol:cllc:clolcloollcclllccclolccclolcccloooololc;,',;,'.  ....      
                           ....''......',cccllllcllooolc::::ccloc:coollllllcccllllllllollllolloololc:::::::.            
                                         .',,;:::clllllllllooollc:cccc:;,'.....',;:clllooooooooooolc;''',,'.            
                                               ....''',;::cllllc:,,'...           ...':lc::::::::::;;,.                 
                                                          ..''..                      .';;,,,,,,,,,,;:.                 
                                                                                        .'::;;:;;;:;::.                 
                                                                                          .,:::;;;;;::.                 
                                                                                            .';:;,,,,;.                 
                                                                                              .';;;,,;.                 
                                                                                                 ';,,'.                 
                                                                                                   .                    
                                                                                                                        
            """
        case 2:
            nave = """
                                                                                                 .....                  
                                                                                               .'    ;.                 
                                                                                              ':;,  ;;.                 
                                                                                           .';;*#,,,;:.                 
                                                                                          ';:;;,   ,;;.                 
                                                                                       .';:;,,,,  ,,;:.                 
                                                     ....',::  ,...                  .'::;;;;;;;;;;;:;.                 
                                          ....''',;:::clllllllllccc:;,'...     ...',;ccllllloollollc;'.....             
                                        .;cccllccclllllllcclllloc:clllccc:;'',;cc  llllooolooloooolc;;;;::;.            
                               ::;,'',;:cccllooocclololc:c:::clolcclolllllllccclll  ccllllccloooooooc;;;:::;.            
                           llllllllllllllloooooolclllol:cllc;cllc:clolccclolccclll  cclllcccllllooolc:,',,,'...',,'..    
                           ooooooooooooooolooloolllcloolc:::::clolclooollllcllcclcc  llllllcccllooll:,;;;,,,,:::::.      
   .:clllllllloooooooooooooooooooooooooollllllllcccccllllcllccllollllclllccclllll  llllllllclccllcc:;:::;'...''..       
  .,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'''''''''''''''''''''',:ccccccccccccclo  lllllllcllllcllc:cccccllllcc:ccc::,.  
  .'............................................................,clllllllllllcclollllllllllllllllcclllllccllllllccccc.  
  .#*''''''''''''''''''''''''''''''''''........................';cccccllcclccccllllllllllllllllllcccllccclllllllllllc.  
  .,:ccccccccccccccccccclccccccccccccccc:;;;;;;;;;;;;;;;;;;;;;;:clllccccccccclloollllllllcclclllccccccccccc;,',,,,'..   
    .,::cccllcllllllooooolooollooooololoooooooooollclooolcclloolllloll            ccllllllllcclccloll:;;;;,...',,,'.    
       ....''',;:::clllllllllllooollllloolollooolccloolc:::::cllc:c     @#*  @#*     lllcccllcllloolc;,,,,',,,;:::;.    
                  ...''',;:::clllc::cclllllooloolclolol:cllc             @#*     olcclolcccloooololc;,',;,'.  ....      
                           ....''......',cccllllcllooolc::::ccloc:coollllllc                lloololc:::::::.            
                                         .',,;:::clllllllllooollc:cccc:;,'.....',;:clllooooooooooolc;''',,'.            
                                               ....''',;::cllllc:,,'...           ...':lc::::::::::*#,.                 
                                                          ..''..                      .';;,,,,,,, ,#:.                 
                                                                                        .'::;;:;; #::.                  
                                                                                          .,:::;; *::.                  
                                                                                            .';:; ,,;.                  
                                                                                              .';;;,,;.                 
                                                                                                 ';,,'.                 
                                                                                                   .
            """
        case 3:
            nave = """
                                                                                                 .....                  
                                                                                               .      .                 
                                                                                              ':,    ;.                 
                                                                                           .';;       .                 
                                                                                          ';:;;, ,  ;;.                 
                                                                                       .';:;,, ,,,,,;:.                 
                                                     ... *#@%,...                    .'::;;;;; ;;;;;:;.                 
                                          ....''',;:::cllllllll                *#@%  ;cclllllloollollc;'.....           
                                        .;cccllccclllllllccllllo              #@@%* llllllooolooloooolc;;;;::;.       
                                   '',;:cccllooocclololc:c:::clol            *#@%      lllccllllccloooooooc;;;:::;.      
                         clllllllllllllllloooooolclllol:cllc;cllc:          #@%        llccclllcccllllooolc:,',,,'...   
                         llooooooooooooooolooloolllcloolc:::::clol        *#@          clccccllllllllcccllooll:,;;;,,   
     **#@% lloooooooooooooooooooooooooollllllllcccccllllcllccllo        *#@%           lllllllllllllclccllcc:;:::;'...  
     *%@ ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'''''''''''''''''''''',:c       #@%              llllllllcllllcllc:cccccllllc   
     ...#.....................................................,c      *#@              lllllllllllllcclllllccllllllcc   
     ''''''#****************'''''............................';cc    #@%               lllllllllllcccllcccllllllllll    
     ccccccccccclccccccccccccccc:;;;;;;;;;;;;;;;;;;;;;;:clllccccc   #@                 lllllllcclclllccccccccccc;,',,   
      ::cccllcllllllooooolooollooooololoooooooooollclooolcclloollllol                  lllllclccloll:;;;;,...',,,'.     
        ...''',;:::clllllllllllooollllloolollooolccloolc:::::cllc:clo                  cccllcllloolc;,,,,',,,;:::;.     
                  ...''',;:::clllc::cclllllooloolclolol:cllc:clolcloo                  cccloooololc;,',;,'.  ....       
                           ....''......',cccllllcllooolc::::ccloc:coo                  lllolloololc:::::::.             
                                         .',,;:::clllllllllooollc:ccc                  oooooooooolc;''',,'.             
                                               ....''',;::cllllc:,,'...                :lc::::::::::;;,.                
                                                          ..''..                       ;;,,,,,,,,,,;:.                  
                                                                                       *#%*;;;:;::.                     
                                                                                        *#@%*;;;::.                     
                                                                                          *%@*,,;.                      
                                                                                              .';;;,,;.                 
                                                                                                 ';,,'.                 
                                                                                                   .
            """
        case 4:
            nave = """
                                                                                                 ..#..                  
                                                                                               . *#%* .                 
                                                                                              ':, #@ ;.                 
                                                                                           .';;  #%   .                 
                                                                                          ';:;;, @  ;;.                 
                                                                                       .';:;,, %,,,,;:.                 
                                                     *#@%#* .'::;;;;; ;;;;;:;.                 
                                          ..*#@%*;;:::cllllllll                *#@%  ;cclllll *#@ llollc;'.....          
                                        .*#@@%:clccclllllllcclllo             #@@%* lllll   #@@%*#@  ooolc;;;;::;.    
                      ..*#@@%*''',;::;,'',;:cccllooocclololc:c:::clol        *#@%      lll     *#@@@@%*#   oooooc;;;::. 
            .*#@@@%#**;:cccllllllllllllllllloooooolclllol:cllc;cllc:        #@%         :#lc        *#@@@%#** looolc:,',  
      ..*#,;*#@@#*llllclllllllllllooooooooooooooolooloolllcloolc:::::clol  *#@                     *#@@#* looll:,;;;    
      **#@%  *#@%#*:ooooooooooooooooooooooollllllllcccccllllcllccllo      *#@%                      *#@%#             l 
*#@%#* *%@    *#@@#*;;;;;;;;;;;;;;;;;;,,'''''''''''''''''''''',:c        #@%                       *#@@#* llcc:ccc::    
#@@@%****#@%    *#@@%**.........................................,c      *#@                         *#@@%**clll         
*%@@@@#*''''''    *#@# ........................................';cc    #@%                            *#@# cllllll      
     ccccccccccclcccc*#     ccccc:;;;;;;;;;;;;;;;;;;;;;;:clllccccc   #@                                 *#       ccl    
      ::cccllcllllllooo*@* llooooololoooooooooollclooolcclloollllol                                     *#@* llllc l   
        ...''',;:::clllll*#@*llloollllloolollooolccloolc:::::cllc:clo                                      *%@* lllcc   
                  ...''',;*#  *::cclllllooloolclolol:cllc:clolcloo                                          *#  ccclo   
                           ..#  .......',cccllllcllooolc::::ccloc:co                                        *#@* ollll  
                                 * .',,;:::clllllllllooollc:cc                                       *#%* ooooo   
                                               ....''',;::cllllc:,,'...                                    :lc::::::::  
                                                          ..''..                                           ;;,,,,,,,,,  
                                                                                                           *#%*;;;:;::  
                                                                                                            *#@%*;;;::  
                                                                                                              *%@*,,;.  
                                                                                                                 *#%* ** .
            """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in nave.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def masc_resistencia(s):
    match s:
        case 1:
            nave = """
                ......................................................................................................................................................
                ......................................................'...............''..............................................................................
                ................................................';:loddo,.;lllllll;..lxxdlc::,........................................................................
                ............................................';cdxxdddddo,.;::cccc:;.'odddddxxkxo:,....................................................................
                .........................................':oddoodddxkkkkc,:;cxxxx:,,;xkkxddddoooxxdc'.................................................................
                .......................................;ccooooclkkOkkkxdc':;cdddd:,';dkkOOkOkdclooolloc'..............................................................
                .....................................'cdoloxkOxloxdollodl'',;c:::;'':ddoooddocokOkdlldkxl,............................................................
                .......................................'ckOkkkkxooocokkOx;,;;;:;:;''oOkxllooloxkkOkkxoodkxl'..........................................................
                .................................,'.....,:okOkkkkOkdlxkkkc',:cccl:.,dOkookOkkkkkkkkkkkxocokxc,,:;'....................................................
                ............................. .;ll:;c:;,,,,:okOOkkOkolxkkl'.:lccl;.,xkocxkkkkOkkkkkkkxoc::lxko;;odoc,.................................................
                ..............................:ol;:locclc:;'.;okkxolc;lxOd'.:cccl:.;xdlooodxkOkkOkkko::cllccdkd;;ll;;;,';;'...........................................
                ........................... .:oc:od:;coxkx:...':oo::lc;col'.:c::l;.;l:okx:coxOkkkkdolc:clllc:lol,,'.,,'.:ddoc,........................................
                ............................:oc:dx:''..';ldlc;'.':c::llclx;.co:cd:.;clooclxkkkkxooodxdl:cccc:cokd;.,,,,;lddc;;;,,;,'..................................
                ......................... .;oc:dxc,,......;cc;,;;'',lkOdcoc.ckkkk:.;dkkxdooddoooodxxxxdc:lodxkkkOd,;llodddo,.,,''cddoc;,..............................
                ......................... 'll;okkl;:,.....,....':c;'':dkol:',llll,.ckkkkOkdoccdxxxddooddxkOOOOOOOk:'cdddodo:,'',;ldooddolc;,'.........................
                ..........................:o;;lll::odolc;,'......;c;,;;::;,';:;'',,:lxkOOOOOxlcoooddkkOxddddddddddl,':cccccc:;;:ccccccccccccll'.......................
                ........................ .,,;dkxdoc:cllc:ll;''.',:::l:'':oo::ll,:do;';oxxdooooodxkkkkxolcllodxxxxkkc.'''''''',;::::::::::;,',,........................
                .........................,:.,okkkkdldxdolllc::ccol:c:.'clc:codl,,c::c:,:c;;ccllllllll::::c::cllllll:,'''''''..........................................
                ....................... .;;..cdccc;,,:clc:;,',;:c:,;''ccc::c;,'...';cl:,::cdddolcc:ccccccccllllll:;;;;;;,;oo,.........................................
                .........................;;..cl,,......'......'cdc'''cdddddl,. .;:,'';,..':c:llcllclclllocc::c:::'...... .co,.........................................
                .........................;;..cl,'......,'.....':o:''':ddoolc'...,;'',:;'.,:lclodddddddddddolllclc'...... .co,.........................................
                .........................;;..cdlcc;,;codol;'';:cl:,;'':cc:;:::;'''':cl:,:;:ooolloooooloooolloolol:;;;;;;;:ll'.........................................
                ..........................,.'collcloooollll:;;::ll:cc',lddlccll,;oc::;,;:,,;:clllllllc;;;:;:lllllll:..................................................
                ........................ .,;,;c::;:lllolcc:'....,;::cc,';cc:cll;;ol;',:c:cc:cclodxkkOkxlcllodddddxx:.',,,,,,,;::::::::::::;;;:'.......................
                ..........................;o:,cooc:ooc;;''......':c;',:lc;'';::,,'.,:;,'.':cc:looooddxkkxdxxxxddddc',cccccc:,'',;cccccccccc::;........................
                ......................... .ll:lkkl;;'.....,'.'';c:,',lxxllc':dddx;..,,,,'...':oddxxxdddooxkkOkkkOk:,odddddo;.''',ldddddoc;,...........................
                ...........................,ol:oxc,,.....':ooc,,'',,cxkocd:.cxddx: .',,,;;;;,,cooodxxxxlcooooxkkkl';c:clddo,.''.'col:,'...............................
                ............................,ol:oxl''';:coo:;,..,cllool:lo,.:l;;l;..',::,.';;,,coooodolokOxo::odl'..''''cddoc:,'''....................................
                ........................... .;ol:coc;:okkd,...,lxocoxxlodl..:clcc;.,l;;c;....;c;;oxdccdkkkkoldxc';,.'''':ol:,'........................................
                ..............................,oo:;coc::::,',lxkkkxdlcokOo'.:lccl;.;xd,':c,...;:;,cxxoodkxooxkl,:doc:;'.'.............................................
                ............................. .'cl;',;,',,;lxkkkkkkkookkkl'.:olll;.,dko''cc;'..'cl;;okxocldkxc,col:,'.................................................
                ........................................,lxkkkOkxkkooxkOk:',:c:cl:.,oOkl..:ll:..':c;,:oooxkl,.,,......................................................
                ......................................,:lxkkkkkdcllcldxkx;';;::;:;''lkdo:',;co:...,ll,.cxo;...........................................................
                ......................................:docldxkdcoddoccloc',,:lccl;'';olldxc,,;cc,..;cc;''.  ..........................................................
                ........................................,:odooccoddddddd:'::lkkkxc;,:kkkOOkxc':ol'..'::,,;............................................................
                ..........................................':lddooolllooo;.;,;lool;,',dxdddodoc,,cc;.....,c'.,'.';,....................................................
                ..............................................,:ldxddool,.;ccclllc:.'ldddxxxxo;.,od:....'c'.,,',:;....................................................
                ..................................................';:clc'.':::::::'..:llc;,''....,c::ll;;c,.''........................................................
                ....................................................................................,;,'.'............................................................
                ......................................................................................................................................................
            """
        case 2:
            nave = """
                ......................................................................................................................................................
                ......................................................'...............''..............................................................................
                ................................................';:loddo,.;lllllll;..*#@%#*...........................................................................
                ............................................';cdxxdddddo,.;::cccc:;.'o*#@%#*:,........................................................................
                .........................................':oddoodddxkkkkc,:;cxxxx:,,;xkkxddddooxxdc'.................................................................
                .......................................;ccooooclkkOkkkxdc':;cdddd:,';dkkOOkOkdclooolloc'..............................................................
                .....................................'cdoloxkOxloxdollodl'',;c:::;'':ddoooddocokOkdlldkxl,............................................................
                .......................................'ckOkkkkxooocokkOx;,;;;:;:;''oOkxllooloxkkOkkxoodkxl'..........................................................
                .................................,'.....,:okOkkkkOkdlxkkkc',:cccl:.,dOkookOkkkkkkkkkkkxocokxc,,:;'....................................................
                ............................. .;ll:;c:;,,,,:okOOkkOkolxkkl'.:lccl;.,xkocxkkkkOkkkkkkkxoc::*#@%#*.......................................................
                ..............................:ol;:locclc:;'.;okkxolc;lxOd'.:cccl:.,xdlooodxkOkkOkkko::cllc*#@%#*......................................................
                ........................... .:oc:od:;coxkx:...':oo::lc;col'.:c::l;.,l:okx:coxOkkkkdolc:clllc:*#@%#*...................................................
                ............................:oc:dx:''..';ldlc;'.':c::llclx;.co:cd:.,clooclxkkkkxooodxdl:cccc:c*#@%#*..................................................
                ......................... .*#@%#*.........;cc;,;;'',lkOdcoc.ckkkk:.,dkkxdooddoooodxxxxdc:lodxkkkOd,;llodddo,.,,''cddoc;,..............................
                ......................... *#@%#*..........,....':c;'':dkol:',llll,.ckkkkOkdoccdxxxddooddxkOOOOOOOk:'cdddodo:,'',;ldooddolc;,'.........................
                ..........................:o;;lll::odolc;,'......;c;,;;::;,';:;'',,:lxkOOOOOxlcoooddkkOxddddddddddl,':cccccc:;;:ccccccccccccll'.......................
                ........................ .,,;dkxdoc:cllc:ll;''.',:::l:'':oo::ll,:do;';oxxdooooodxkkkkxolcllodxxxxkkc.'''''''',;::::::::::;,',,........................
                .........................,:.,okkkkdldxdolllc::ccol:c:.'clc:codl,,c::c:,:c;;ccllllllll::::c::cllllll:,'''''''..........................................
                ....................... .;;..cdccc;,,:clc:;,',;:c:,;''ccc::c;,'...';cl:,::cdddolcc:ccccccccllllll:;;;;;;,;oo,.........................................
                .........................;;..cl,,......'......'cdc'''cdddddl,. .;:,'';,..':c:llcllclclllocc::c:::'...... .co,.........................................
                .........................;;..cl,,......,'.....':o:''':ddoolc'...,;'',:;'.,:lclodddddddddddolllclc'...... .co,.........................................
                .........................;;..cdlcc;,;codol;'';:cl:,;'':cc:;:::;'''':cl:,:;:ooolloooooloooolloolol:;;;;;;;:ll'.........................................
                ..........................,.'collcloooollll:;;::ll:cc',lddlccll,;oc::;,;:,,;:clllllllc;;;:;:lllllll:..................................................
                ........................ .,;,;c::;:lllolcc:'....,;::cc,';cc:cll;;ol;',:c:cc:cclodxkkOkxlcllodddddxx:.',,,,,,,;::::::::::::;;;:'.......................
                ..........................;o:,cooc:ooc;;''......':c;',:lc;'';::,,'.,:;,'.':cc:looooddxkkxdxxxxddddc',cccccc:,'',;cccccccccc::;........................
                ......................... .ll:lkkl;;'.....,'.'';c:,',lxxllc':dddx;..,,,,'...':oddxxxdddooxkkOkkkOk:,odddddo;.''',ldddddoc;,...........................
                ...........................,ol:oxc,,.....':ooc,,'',,cxkocd:.cxddx: .',,,;;;;,,cooodxxxxlcooooxkkkl';c:clddo,.''.*#@%#*...............................
                ............................,ol:oxl''';:coo:;,..,cllool:lo,.:l;;l;..',::,.';;,,coooodolokOxo::odl'..''''cddoc:,'''....................................
                ........................... .;ol:coc;:okkd,...,lxocoxxlodl..:clcc;.,l;;c;....;c;;oxdccdkkkkoldxc';,.'''':ol:,'........................................
                ..............................,oo:;coc::::,',lxkkkxdlcokOo'.:lccl;.,xd,':c,...;:;,cxxoodkxooxkl,:doc:;'.*#@%#*........................................
                ............................. .'cl;',;,',,;lxkkkkkkkookkkl'.:olll;.,dko''cc;'..'cl;;okxocldkxc,col:,'.................................................
                ........................................,lxkkkOkxkkooxkOk:',:c:cl:.,oOkl..:ll:..':c;,:oooxkl,.,,......................................................
                ......................................,:lxkkkkkdcllcldxkx;';;::;:;''lkdo:',;co:...,ll,.cxo;...........................................................
                ......................................:docldxkdcoddoccloc',,:lccl;'';olldxc,,;cc,..*#@%#*.............................................................
                ........................................,:odooccoddddddd:'::lkkkxc;,:kkkOOkxc':ol'..*#@%#*............................................................
                ..........................................':lddooolllooo;.;,;lool;,',dxdddodoc,,cc;.....,c'.,'.';,....................................................
                ..............................................,:ldxddool,.;ccclllc:.'ldddxxxxo;.,od:....'c'.,,',:;....................................................
                ..................................................';:clc'.':::::::'..:llc;,''....,c::ll;;c,.''........................................................
                ....................................................................................,;,'.'............................................................
                ......................................................................................................................................................
            """
        case 3:
            nave = """
                ......................................................................................................................................................
                ......................................................'...............''..............................................................................
                ................................................';:loddo,.;lllllll;..*#@%#*...........................................................................
                ............................................';cdxxdddddo,.;::*#@%#*...................................................................................
                .........................................':oddoodddxkkkkc,:;cxxxx:,,;xkkx*#@%#*.......................................................................
                .......................................;ccooooclkkOkkkxdc':;cdddd:,';dkkOOkOkdclooolloc'..............................................................
                .....................................'cdoloxkOxloxdollodl'',;c:::;'':ddoooddocokOkdlldkxl,............................................................
                .......................................'ckOkkkkxooocokkOx;,;;;:;:;''oOkxllooloxkkOkkxoodkxl'..........................................................
                .................................,'.....,:okOkkkkOkdlxkkkc',:cccl:.,dOkookOkkkkkkkkkkkxocokxc,,:;'....................................................
                ............................. .;ll:;c:;,,,,:okOOkkOkolxkkl'.:lccl;.,xkocxkkkkOkkkkk*#@%#*.............................................................
                ..............................*#@%#*..................................*#@%#*..........................................................................
                ........................... *#@%#*......................................*#@%#*........................................................................
                ............................*#@%#*......................................*#@%#*........................................................................
                ......................... *#@%#*...................lkOdcoc.ckkkk:.,dkkxdooddoooodxxxxdc:*#@%#*........................................................
                ......................... *#@%#*...................',llll,.ckkkkOkdoccdxxxddooddxkOOOOO*#@%#*........................................................
                ..........................*#@%#*.................';:;'',,:lxkOOOOOxlcoooddkkOxddddddddd*#@%#*........................................................
                ........................ .*#@%#*...............:ll,:do;';oxxdooooodxkkkkxolcllodxxxxkkc*#@%#*........................................................
                .........................,*#@%#*..............codl,,c::c:,:c;;ccllllllll::::c::cllllll:*#@%#*........................................................
                ....................... .;;..cdccc;,,:clc:;,',;:c:,;''ccc::c;,'...';cl:,::cdddolcc:ccccccccllllll:;;;;;;,;oo,.........................................
                .........................;;..cl,,......'......'cdc'''cdddddl,. .;:,'';,..':c:llcllclclllocc::c:::'...... .co,.........................................
                .........................;;..cl,,......,'.....':o:''':ddoolc'...,;'',:;'.,:lclodddddddddddolllclc'...... .co,.........................................
                .........................;;..cdlcc;,;codol;'';:cl:,;'':cc:;:::;'''':cl:,:;:ooolloooooloooolloolol:;;;;;;;:ll'.........................................
                ..........................,.'collcloooollll:;;::ll:cc',lddlccll,;oc::;,;:,,;:clllllllc;;;:;:lllllll:..................................................
                ........................ .,;,;c::;:lllolcc:'....,;::cc,';cc:cll;;ol;',:c:cc:cclodxkkOkxlcllodddddxx:.',,,,,,,;::::::::::::;;;:'.......................
                ..........................;o:,cooc:ooc;;''......':c;',:lc;'';::,,'.,:;,'.':cc:looooddxkkxdxxxxddddc',cccccc:,'',;cccccccccc::;........................
                ......................... .ll:lkkl;;'.....,'.'';c:,',lxxllc':dddx;..,,,,'...':oddxxxdddooxkkOkkkOk:,odddddo;.''',*#@%#*...............................
                ...........................,ol:oxc,,.....':ooc,,'',,cxkocd:.cxddx: .',,,;;;;,,cooodxxxxlcooooxkkkl';c:clddo,.''.*#@%#*...............................
                ............................,ol:oxl''';:coo:;,..,cllool:lo,.:l;;l;..',::,.';;,,coooodolokOxo::*#@%#*.................................................
                ........................... .;ol:coc;:okkd,...,lxocoxxlodl..:clcc;.,l;;c;....;c;;oxdccdkkkkoldxc'*#@%#*...............................................
                ..............................,oo:;coc::::,',lxkkkxdlcokOo'.:lccl;.,xd,':c,...;:;,cxxoodkxooxkl,*#@%#*................................................
                ............................. .'cl;',;,',,;lxkkkkkkkookkkl'.:olll;.,dko''cc;'..'cl;;okxocldkxc,*#@%#*.................................................
                ........................................,lxkkkOkxkkooxkOk:',:c:cl:.,oOkl..:ll:..':c;,:oooxkl,.,,......................................................
                ......................................,:lxkkkkkdcllcldxkx;';;::;:;''lkdo:',;co:...,ll,.cxo;...........................................................
                ......................................:docldxkdcoddoccloc',,:lccl;'';olldxc,,;cc,..*#@%#*.............................................................
                ........................................,:odooccoddddddd:'::lkkkxc;,:kkkOOkxc':ol'..*#@%#*............................................................
                ..........................................':lddooolllooo;.;,;lool;,',dxdddodoc,,cc;.....,c'.,'.';,....................................................
                ..............................................,:ldxddool,.;ccclllc:.'ldddxxxxo;.,od:....'c'.,,',:;....................................................
                ..................................................';:clc'.':::::::'..:llc;,''....,c::ll;;c,.''........................................................
                ....................................................................................,;,'.'............................................................
                ......................................................................................................................................................
            """
        case 4:
            nave = """
                ......................................................................................................................................................
                ......................................................*#@%#*..........*#@%#*..........................................................................
                ................................................*#@%#*................*#@%#*..........................................................................
                ............................................*#@%#*....................*#@%#*..........................................................................
                .........................................*#@%#*:,:;cxxxx:,,;xkkxddddooxxdc'............................................................................
                .......................................;ccooooclkkOkkkxdc':;cdddd:,';dkkOOkOkdclooolloc'..............................................................
                .....................................'cdoloxkOxloxdollodl'',;c:::;'':ddoooddocokOkdlldkxl,............................................................
                .......................................'ckOkkkkxooocokkOx;,;;;:;:;''oOkxllooloxkkOkkxoodkxl'..........................................................
                .................................,'.....,:okOkkkkOkdlxkkkc',:cccl:.,dOkookOkkkkkkkkkkkxocokxc,,:;'....................................................
                ............................. .;ll:;c:;,,,,:okOOkkOkolxkkl'.:lccl;.,xkocxkkkkOkkkkkkkxoc::lxko;;odoc,.................................................
                ..............................*#@%#*..................................*#@%#:oxkkOkkko::cllccdkd;;ll;;;,';;'...........................................
                ........................... *#@%#*......................................*#@%#*........................................................................
                ............................*#@%#*......................................*#@%#*........................................................................
                ......................... *#@%#*...................lkOdcoc.ckkkk:.;dkkxdooddoooodxxxxdc:*#@%#*........................................................
                ......................... *#@%#*...................',llll,.ckkkkOkdoccdxxxddooddxkOOOOO*#@%#*........................................................
                ..........................*#@%#*.................';:;'',,:lxkOOOOOxlcoooddkkOxddddddddd*#@%#*........................................................
                ........................ .*#@%#*...............:ll,:do;';oxxdooooodxkkkkxolcllodxxxxkkc*#@%#*........................................................
                .........................,*#@%#*..............codl,,c::c:,:c;;ccllllllll::::c::cllllll:*#@%#*........................................................
                ....................... .*#@%#*............,;''ccc::c;,'...';cl:,::cdddolcc:cccccccclll*#@%#*........................................................
                .........................*#@%#*............'cdc'''cdddddl,. .;:,'';,..':c:llcllclcllloc*#@%#*........................................................
                .........................*#@%#*............':o:''':ddoolc'...,;'',:;'.,:lcloddddddddddd*#@%#*........................................................
                .........................*#@%#*............';:cl:,;'':cc:;:::;'''':cl:,:;:ooolloooooloo*#@%#*........................................................
                ..........................*#@%#*...........:;;::ll:cc',lddlccll,;oc::;,;:,,;:clllllllc;*#@%#*........................................................
                ........................ .*#@%#*....................,;::cc,';cc:cll;;ol;',:c:cc:cclodxk*#@%#*........................................................
                ..........................*#@%#*......................':c;',:lc;'';::,,'.,:;,'.':cc:loo*#@%#*........................................................
                ......................... *#@%#*........................,lxxllc':dddx;..,,,,'...':oddxxx*#@%#*........................................................
                ...........................*#@%#*.......................cxkocd:.cxddx: .',,,;;;;,,coood*#@%#*........................................................
                ............................*#@%#*......................:lo,.:l;;l;..',::,.';;,,coooood*#@%#*........................................................
                ........................... .*#@%#*.....................odl..:clcc;.,l;;c;....;c;;oxdcc*#@%#*........................................................
                ..............................*#@%#*....................kOo'.:lccl;.,xd,':c,...;:;,cxxoo*#@%#*........................................................
                ............................. *#@%#*....................kkl'.:olll;.,dko''cc;'..'cl;;okx*#@%#*........................................................
                ........................................................kOk:',:c:cl:.,oOkl..:ll:..':c;,:*#@%#*........................................................
                ........................................................dxkx;';;::;:;''lkdo:',;co:...,l*#@%#*..........................................................
                ........................................................*#@%#*........................*#@%#*..........................................................
                ........................................................*#@%#*......................*#@%#*............................................................
                ..........................................................*#@%#*..................*#@%#*..............................................................
                ..............................................................*#@%#*............*#@%#*................................................................
                ..................................................................*#@%#*....*#@%#*....................................................................
                ....................................................................................,;,'.'............................................................
                ......................................................................................................................................................
            """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in nave.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



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
                print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
                continue
        except:
            print(f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌')
            continue



def texto_star_wars(texto, nud=11, nur=61):
    pygame.mixer.init()
    som_digitando = pygame.mixer.Sound("digitando.ogg")
    som_digitando.play(-1)
    largura_terminal = shutil.get_terminal_size().columns
    linha_centralizada = texto.center(largura_terminal)
    x = 1
    y = 0
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
    time.sleep(1)
    print()
    som_digitando.stop()



def texto_star_wars_sem_musica(texto, nud=11, nur=61):
    largura_terminal = shutil.get_terminal_size().columns
    linha_centralizada = texto.center(largura_terminal)
    x = 1
    y = 0
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
    print()



def showMatriz_nbidsfn(matriz):
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



def mostrar_nave(nave, vida, paramet):
    if vida > (paramet * 3):
        x = 1
    elif vida > (paramet * 2):
        x = 2
    elif vida > (paramet * 1):
        x = 3
    else:
        x = 4
    
    if nave == 1:
        masc_resistencia(x)
    elif nave == 2:
        masc_imperio(x)



if __name__ == '__main__':
    pass
