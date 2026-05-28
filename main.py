import time
import shutil
import os
import pygame

def main():
    pygame.mixer.init()
    pygame.mixer.music.load('Star-Wars-Main-Theme-_Full_.ogg') 
    pygame.mixer.music.play()
    time.sleep(2) 
    
    os.system('cls')
    texto_abertura = """
    EPISÓDIO I
    UMA HISTÓRIA STAR WARS

    É um tempo de tirania sombria. Por décadas, o pacífico povo Gungan foi subjugado pela opressão
    implacável do IMPÉRIO GALÁCTICO. Encorajados pela coragem e liderança da PRINCESA LEIA
    ORGANA, os outrora reclusos Gungans finalmente se levantaram em uma rebelião desesperada,
    clamando por liberdade em seu próprio mundo natal.

    Nas profundezas dos oceanos de Naboo, as outrora brilhantes cidades submarinas
    agora jazem na escuridão. O grito de revolta ecoou pelos pântanos e planícies,
    unindo os clãs Gungans sob uma única bandeira de resistência, jurando expulsar as
    guarnições imperiais que profanam suas terras sagradas.

    A retaliação imperial, porém, foi imediata e cruel. Sob as ordens de oficiais
    implacáveis, o Império estabeleceu um bloqueio orbital absoluto, cortando todo o
    fornecimento de água potável e mantimentos para a superfície e para as
    profundezas. A fome e a sede assolam a população, ameaçando extinguir a cultura
    Gungan antes mesmo que a verdadeira guerra comece.

    Enquanto o desespero consome o planeta, a resistência clandestina luta contra o
    relógio para manter acesa a última chama de esperança. Mensagens codificadas
    são enviadas para os confins da galáxia, mas poucos ousam desafiar a frota de
    Destroieres Estelares que vigia os céus de Naboo como predadores famintos.

    Em uma missão de pura misericórdia e alto risco, a audaciosa EQUIPE DELTA foi
    designada pela Princesa Leia para romper o cerco. Transportando toneladas de
    suprimentos vitais em um cargueiro corelliano camuflado, o grupo de rebeldes
    traçou uma rota perigosa, confiando cegamente nas coordenadas de infiltração
    fornecidas por um informante local.

    Mas o destino reservava uma armadilha terrível. Uma traição vil nos altos escalões
    da resistência entregou os planos exatos da operação aos comandantes imperiais.
    Ao chegarem na ESTAÇÃO DE POUSO 4, os heróis foram recebidos pelo fogo
    cruzado de uma guarnição inteira de Stormtroopers, transformando a missão de
    resgate em um pesadelo de fumaça e lasers.

    Em meio ao caos do combate e demonstrando uma bravura inacreditável, a Equipe
    Delta conseguiu descarregar os mantimentos nos dutos de ventilação que levavam
    direto às colônias Gungans, garantindo a sobrevivência temporária dos inocentes.
    Mas o preço do sucesso foi alto: os escudos da nave rebelde foram desintegrados e
    o hiperpropulsor começou a falhar.

    Agora, com os alarmes de emergência ecoando pela cabine e caças TIE caçando
    sua assinatura de calor na atmosfera superior, os heróis da Equipe Delta precisam
    realizar uma fuga impossível. Sem apoio e cercados pelas forças inimigas...
    """

    # Largura atual do terminal do VS Code
    largura_terminal = shutil.get_terminal_size().columns
    # Empurra o texto para baixo inicialmente
    print("\n" * 15)
    for linha in texto_abertura.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)
        time.sleep(2)
    
    for n in range(0, 36):
        time.sleep(1)
        print()
    os.system('cls')

if __name__ == '__main__':
    main()
