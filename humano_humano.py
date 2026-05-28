import funcoes

def humano_humano():
    mA = funcoes.matriz10()
    mB = funcoes.matriz10()
    print("\nVocê faz parte da Resistência!")

    funcoes.showMatriz(mA)

    print("\nVocê tem 3 opcções de arma:")
    
    cont = 0

    while cont < 5:
        print("-"*45)
        funcoes.show_armas()
        print("-"*45)
        print("\nobs.: Você deverá posicionar pela ponta delas: ◀")

        try:
            n = int(input('Digite a númeração da arma: '))
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
                        verf = funcoes.colocar_arma2(mA, x, y)
                        funcoes.showMatriz(mA)
                    cont +=1
                    
                case 2:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(2)
                        y = funcoes.verif_cordenada_Y(0)
                        verf = funcoes.colocar_arma3(mA, x, y)
                        funcoes.showMatriz(mA)
                    cont +=1
                    
                case 3:
                    while verf == False:
                        x = funcoes.verif_cordenada_X(3)
                        y = funcoes.verif_cordenada_Y(1)
                        verf = funcoes.colocar_arma4(mA, x, y)
                        funcoes.showMatriz(mA)
                    cont +=1
                    
        else:
            print('Digite nova mente, houve um erro')
            continue


humano_humano()
