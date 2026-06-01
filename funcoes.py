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



if __name__ == '__main__':
    pass
