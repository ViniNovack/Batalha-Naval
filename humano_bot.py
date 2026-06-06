import funcoes
import time
import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import random
import funcoes_imagens
import funcoes


fu = funcoes
fi = funcoes_imagens

class Cores:                              # Mensagemn de erro padrão: f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌'
    # VERMELHO
    vermelho = '\033[31m'
    # LIMPAR
    limpar = '\033[m'
c1 = Cores()



def humano_bot():
    mH = funcoes.matriz10()
    mR = funcoes.matriz10()

    vidaR = 0
    vidaH = 0
#______________________________________________________ABERTURA________________________________________________
    time.sleep(1)
    fu.texto_star_wars('AGORA ESCOLHA UM LADO E DECIDA O DESTINO DESSA HISTÓRIA...\n')
    
    time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load('Audio_-Star-Wars-Epic.ogg') 
    pygame.mixer.music.play()
   
    fi.escudos_lado_a_lado()
    opcao = fu.verif_int('» ', 3)
    pygame.mixer.music.stop()
#________________________________________________________________ESCOLHA DE SER O IMPERIO_____________________________________________________
    if opcao == 1:
        os.system('cls')
        pygame.mixer.init()
        pygame.mixer.music.load('Star-Wars-Imperial-March.ogg')
        pygame.mixer.music.play(-1)
        fu.texto_star_wars_sem_musica("Você decidiu ser um comandante do grande e poderoso Império Galático")
        fu.texto_star_wars_sem_musica("Assuma seu posto e extermine essa escória rebelde")
        time.sleep(3)
        os.system('cls')

        #_____________________________________________JOGO____________________________________________

        # HUMANO
        cont = 0
        print()
        fu.texto_star_wars_sem_musica("Você deve posicionar estrategicamente 5 armas para ELIMINAR os rebeldes invasores… PERMANENTEMENTE ")
        time.sleep(2.5)

        vidaH = fu.incluirNaves(mH)
        
        os.system('cls')
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load('Star-Wars-Imperial-March.ogg') 
        pygame.mixer.music.play(-1)
        fu.texto_star_wars_sem_musica('Agora, com todos os canhões posicionados, podemos começar a atacar')
        fu.texto_star_wars_sem_musica('Precisamos impedir que eles passem o bloqueio e entrem no hiperespaço')
        time.sleep(2)
        os.system('cls')
        fi.comandante_imperial()
        fu.texto_star_wars_sem_musica('“General!! Ligue o monitor da nave e vamos começar o ataque”')
        fu.texto_star_wars_sem_musica('"Isso foi uma ORDEM!!"')
        time.sleep(2)
        os.system('cls')
        fu.masc_imperio(1)
        time.sleep(3)
        pygame.mixer.music.stop()
        
        # ROBO
        os.system('cls')
        fu.texto_star_wars('REBELDES!!!')
        pygame.mixer.init()
        pygame.mixer.music.load('audio_batalha_resistencia.ogg') 
        pygame.mixer.music.play(-1)
        time.sleep(2)
        os.system('cls')
        fu.texto_star_wars_sem_musica('Estamos sob fogo pesado de um destróier!!!')
        fu.texto_star_wars_sem_musica('Precisamos ganhar tempo para escapar do bloqueio estelar e entrar no hiperespaço')
        time.sleep(2.5)
        os.system('cls')
        fu.texto_star_wars_sem_musica('Redirecionem a energia dos escudos para os canhões e para os motores')
        fu.texto_star_wars_sem_musica('E mirem as armas para o destróier')
        time.sleep(2.5)
        os.system('cls')
        fu.texto_star_wars_sem_musica('PRECISAMOS CONTRA-ATACAR!!!')
        time.sleep(2.5)
        os.system('cls')
        fi.dentro_da_nave_resistencia()
        cont = 0
        while cont < 5:
            n = random.randrange(1, 4)
            if n in range(1, 4):
                verf = False
                match n:
                    case 1:
                        while verf == False:
                            x = random.randrange(0, 9) 
                            y = random.randrange(0, 10)
                            verf = funcoes.colocar_arma2(mR, x, y, False)
                        cont +=1
                        vidaR +=2
                    case 2:
                        while verf == False:
                            x = random.randrange(0, 8)
                            y = random.randrange(0, 10)
                            verf = funcoes.colocar_arma3(mR, x, y, False)
                        cont +=1
                        vidaR +=3
                    case 3:
                        while verf == False:
                            x = random.randrange(0, 8)
                            y = random.randrange(0, 9)
                            verf = funcoes.colocar_arma4(mR, x, y, False)
                        cont +=1
                        vidaR +=4
            else:
                continue

        time.sleep(3)
        os.system('cls')
        fu.texto_star_wars_sem_musica('“Tudo pronto!!! Armas apostas e energia redirecionada”')
        time.sleep(3)
        os.system('cls')
        fu.masc_resistencia(1)
        time.sleep(3)
        os.system('cls')
        fu.texto_star_wars_sem_musica('VAMOS FUGIR DAQUI !!!')
        time.sleep(2.5)
        pygame.mixer.music.stop()
        os.system('cls')


        # JOGO
        fi.imagem_texto_batalha()
        os.system('cls')

        pygame.mixer.init()
        pygame.mixer.music.load('March-of-the-Resistance.ogg') 
        pygame.mixer.music.play(-1)

        cont = 0
        resul = False
        parametH = round(vidaH / 4)      #"round" aredonda o valor numérico
        parametR = round(vidaR / 4)
        
        while vidaH != 0 or vidaR != 0:
            if cont == 0:
                fu.texto_star_wars_sem_musica("Faça sua primeira jogada nessa história…")
                time.sleep(2.5)
                os.system('cls')
                fu.texto_star_wars_sem_musica('Nave rebelde identificada')
                fu.mostrar_nave(1, vidaR, parametR)
                fu.texto_star_wars_sem_musica('ATAQUEM...')

            # JOGADAS
            fu.showMatriz(mR)
            x = funcoes.verif_cordenada(x)
            y = funcoes.verif_cordenada(y)
            time.sleep(0.5)
            os.system('cls')
            pygame.mixer.music.pause()
            resul = fu.jogadas_ataque(mR, x, y, 1)
            pygame.mixer.music.unpause()
            fu.showMatriz(mR)
            time.sleep(3)
            os.system('cls')

            if resul == True:
                vidaR -=1
                if (parametR * 4) >= vidaR > (parametR * 3):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Eles nos acertaram, mas os escudos estão aguentando por enquanto')
                    fu.texto_star_wars_sem_musica('Se mantenham firmes na trajetória, precisamos quebrar o bloqueio')
                elif (parametR * 3) >= vidaR > (parametR * 2):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Os escudos foram avariados!! Fomos atingidos!! Nosso bico dianteiro está comprometendo a estabilidade da nave…')
                    fu.texto_star_wars_sem_musica('Redirecionem a energia dos propulsores para os escudos, precisamos estar vivos para fugir!')
                elif (parametR * 2) >= vidaR > (parametR * 1):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('OS ESCUDOS CAÍRAM!! Perdemos todo o nosso bico dianteiro e nossa estabilidade junto')
                    fu.texto_star_wars_sem_musica('REDIRECIONEM TODA A ENERGIA PARA OS PROPULSORES E ARMAS, VAMOS GANHAR TEMPO!!!')
                elif (parametR * 1) > vidaR:
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('A nave está totalmente comprometida, além do nosso bico, um dos nossos motores foi totalmente destruído.')
                    fu.texto_star_wars_sem_musica('Vamos manter a esperança…')
                    fu.texto_star_wars_sem_musica('POTÊNCIA MÁXIMA, ESTAMOS QUASE LÁ!!!')
                time.sleep(2)
                os.system('cls')
            elif resul == False:
                if (parametR * 4) >= vidaR > (parametR * 3):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Estamos indo bem!!!')
                    fu.texto_star_wars_sem_musica('O império ainda não nos reconheceu totalmente')
                elif (parametR * 3) >= vidaR > (parametR * 2):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('O IMPÉRIO JÁ NOS RECONHECEU!!')
                    fu.texto_star_wars_sem_musica('Mas estamos bem, mantenha o curso!')
                elif (parametR * 2) >= vidaR > (parametR * 1):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('ESSA FOI QUASE!!')
                    fu.texto_star_wars_sem_musica('Não podemos mais levar danos, MANTENHAM O FOCO!!')
                elif (parametR * 1) > vidaR:
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('É questão de tempo…')
                    fu.texto_star_wars_sem_musica('Não temos mais escudos e um dos motores está totalmente destruído. O que nos resta é resistir…')
                time.sleep(2)
                os.system('cls')


            os.system('cls')
            if (parametR * 4) >= vidaR > (parametR * 3):
                fu.texto_star_wars_sem_musica('Estamos bem!!!')
                fu.texto_star_wars_sem_musica('Vamos contra-atacar, estamos indo bem')
            elif (parametR * 3) >= vidaR > (parametR * 2):
                fu.texto_star_wars_sem_musica('A nave está começando a perder os escudos')
                fu.texto_star_wars_sem_musica('Precisamos ganhar mais tempo!!!')
            elif (parametR * 2) >= vidaR > (parametR * 1):
                fu.texto_star_wars_sem_musica('ESTAMOS SEM ESCUDOS!!!')
                fu.texto_star_wars_sem_musica('Precisamos reagir…')
            elif (parametR * 1) > vidaR:
                fu.texto_star_wars_sem_musica('A NAVE ESTÁ PRATICAMENTE CONDENADA…')
                fu.texto_star_wars_sem_musica('Precisamos furar o bloqueio e entrar no hiperespaço, AGORA!!!')
            time.sleep(2)
            os.system('cls')

            fu.mostrar_nave(2, vidaH, parametH)
            fu.showMatriz(mH)
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
            pygame.mixer.music.pause()
            resul = funcoes.jogadas_ataque(mH, x, y, mH)
            pygame.mixer.music.unpause()
            time.sleep(2)
            os.system('cls')
            fu.mostrar_nave(2, vidaH, parametH)
            fu.showMatriz(mH)
            time.sleep(2)
            os.system('cls')
            if resul == True:
                vidaH -=1
                if (parametR * 4) >= vidaH > (parametR * 3):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Eles nos acertaram, mas os escudos estão aguentando por enquanto')
                    fu.texto_star_wars_sem_musica('Se mantenham firmes na trajetória, precisamos quebrar o bloqueio')
                elif (parametR * 3) >= vidaH > (parametR * 2):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Os escudos foram avariados!! Fomos atingidos!! Nosso bico dianteiro está comprometendo a estabilidade da nave…')
                    fu.texto_star_wars_sem_musica('Redirecionem a energia dos propulsores para os escudos, precisamos estar vivos para fugir!')
                elif (parametR * 2) >= vidaH > (parametR * 1):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('OS ESCUDOS CAÍRAM!! Perdemos todo o nosso bico dianteiro e nossa estabilidade junto')
                    fu.texto_star_wars_sem_musica('REDIRECIONEM TODA A ENERGIA PARA OS PROPULSORES E ARMAS, VAMOS GANHAR TEMPO!!!')
                elif (parametR * 1) > vidaH:
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('A nave está totalmente comprometida, além do nosso bico, um dos nossos motores foi totalmente destruído.')
                    fu.texto_star_wars_sem_musica('Vamos manter a esperança…')
                    fu.texto_star_wars_sem_musica('POTÊNCIA MÁXIMA, ESTAMOS QUASE LÁ!!!')
                time.sleep(2)
                os.system('cls')
            elif resul == False:
                if (parametR * 4) >= vidaH > (parametR * 3):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('Estamos indo bem!!!')
                    fu.texto_star_wars_sem_musica('O império ainda não nos reconheceu totalmente')
                elif (parametR * 3) >= vidaH > (parametR * 2):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('O IMPÉRIO JÁ NOS RECONHECEU!!')
                    fu.texto_star_wars_sem_musica('Mas estamos bem, mantenha o curso!')
                elif (parametR * 2) >= vidaH > (parametR * 1):
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('ESSA FOI QUASE!!')
                    fu.texto_star_wars_sem_musica('Não podemos mais levar danos, MANTENHAM O FOCO!!')
                elif (parametR * 1) > vidaH:
                    fu.texto_star_wars_sem_musica('REBELDES...')
                    fu.texto_star_wars_sem_musica('É questão de tempo…')
                    fu.texto_star_wars_sem_musica('Não temos mais escudos e um dos motores está totalmente destruído. O que nos resta é resistir…')
                time.sleep(2)
                os.system('cls')
            cont +=1
        # FIM
        if vidaH == 0:
            return 1   #IMPERIO VENCEU
        elif vidaR == 0:
            return 2 #RESISTENCIA VENCEU



#__________________________________________________________ESCOLHA DE SER DA RESISTENCIA______________________________________
    elif opcao == 2:
        pass















if __name__ == '__main__':
    humano_bot()
