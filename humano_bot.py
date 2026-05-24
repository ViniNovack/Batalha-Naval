import util
import time
import os

def humano_bot():
    M = util.matriz10()
    A2 = [0,0,"◀","▩",0]
    
    A3 = [0,"◀","▩","▩",0]
    
    A4a = [0,"◀","▩","▩",0]
    A4b = [0,0,0,"▩",0]
    
    print(M)

    print("Escolha as naves que voce quer posicionar: ")
    print(A2 + '\n' + A3 + '\n' + A4a )

humano_bot()
