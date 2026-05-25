import funcoes

def humano_humano():
    matrizA = funcoes.matriz10()
    matrizB = funcoes.matriz10()
    print("\nVocê faz parte da Resistência!")
    print("\nVocê tem 3 opcções de arma:")
    print("-"*45)
    funcoes.show_armas()
    print("-"*45)
    print("\nobs.: Você deverá posicionar pela ponta delas: ◀")
    print("\nPRIMEIRA ARMA")
    funcoes.showMatriz(funcoes.arma2())

    
    
    



humano_humano()
