import util

def humano_humano():
    matrizA = util.matriz10()
    matrizB = util.matriz10()
    print("\nVocê faz parte da Resistência!")
    print("\nVocê tem 3 opcções de arma:")
    print("-"*45)
    util.show_armas()
    print("-"*45)
    print("\nobs.: Você deverá posicionar pela ponta delas: ◀")
    print("\nPRIMEIRA ARMA")
    util.showMatriz(util.arma2())

    
    
    



humano_humano()