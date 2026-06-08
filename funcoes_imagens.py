import shutil
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

class Cores:                              # Mensagemn de erro padrão: f'❌{c1.vermelho} TENTE DE NOVO, resposta INVALIDA {c1.limpar}❌'
    # VERMELHO
    vermelho = '\033[31m'
    # LIMPAR
    limpar = '\033[m'
c1 = Cores()



# EFEITOS SONOROS
# som_explosao = pygame.mixer.Sound("explosao.ogg")
# som_tiro = pygame.mixer.Sound("tiro.ogg")
# som_digitaçao = pygame.mixer.Sound("digitando.ogg")



def titulo():
    titulo = ("""                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
                                                      ...................................................        ...................              ..........................                                                
                                                 ......................................................',.     .,'.................,.            ',..............................                                           
                                               .'..                                                     '.   ..'.                  .'.           '.                            ..'..                                        
                                             .''                                                        '.   .:'                    ''           '.                               .'.                                       
                                            .'.                                                         '.  .,,.                    .,.          '.                                .'.                                      
                                            .,.                                                        .,.  ''.          .,.         .'          '.           ............          .,.                                     
                                            ''             .,................,.         .,'............... .,.          .,;'         .'.         '.           ''        .'.         .,.                                     
                                            .,.            .'..             .'.         .'.               .'.           ''.,.         .,.        '.           ''        .'.         .,.                                     
                                             .'.             .'..           .'.         .'.               ''           .,. .'.         ''        '.           .'..........          ''                                      
                                              .'.              .'.           '.         .,.              .,.          .'.   ''         .,.       '.                               .''.                                      
                                               ..'.             .'.          '.         .,.              '.           .,.   .,.         .,.      '.                             ..'.                                        
                                                 ..'.            .'.         '.         .,.             .'.          .,,.....,'          ''      '.                          .','.                                          
                      .............................'.             ''         '.         .,.            .,.                               .,.     '.           ..              .'....................                        
                      ''.                                         .'        .'.         .,.            ''                                 .'.    '.           ';'.                               .,.                        
                      '.                                          '.        .'.         .,.           .,.                                 .'.    '.           ''..'.                             .'.                        
                      '.                                         .'.        .'.         .,.          .'.           ...............         .,.   '.           '.  ..'.                           .,.                        
                      '.                                       .'..          '.         .,.          .'.          .,............''          .'   '.           '.    ..'.                         .'.                        
                      ''                                   ......           .'.         ',.         .,.          .'.            .'.         .,.  ''          .'.      ..'...                     .'.                        
                      .'......................................               .'.........'.          .'.............              ............'.  .'...........'.         ...........................                        
                                                                          ..                                                                                                                                                
           .  ..    .   .       .          ..  .    .     ..    ....     ;o;      ...     ..     .               ..   .. ..       ..     ...     .           ...     ...         .   ....    .     ...       .              
          ;0:.dd.  ;0l.l0:    .dO,        .ox.:0;  ,Oc  .x0d'  'd0Oc.  :xxdxx;   cKkkl.  .xo    ,Od.        cxc'.od. 'kl.lk'  ld'.do.  ;xxdl.  .dO,        'dxdd,  :xxdxd,  'dc.;O; .lOOo.  'kx.  .d0xxl.   ;Oo.            
          :Xc.kx.  oX000Nd.  .dOOk'       .xXxOX:  ,Ko  .lkx;   '0d.  ;Xo  .dK;  lXOKk.  .Ox.  'kOOd.       oWNKx0k. '0o.o0'  dW0xKx. ,Kx.     oOOk.      .x0,    ;Kd. .x0' '0NkOK:  .xk.  .xOOd. .kx.:Xl  'OOOl            
          ;Kxc0d. .OxoKox0'  lXOxXk.      .x0:dX:  ,Ko  .;lKO.  '0d   'kO:;cOk.  oXdoOl. .Od. .xXkOXl       oKxoxNk. .OOcOO.  d0lxNx. .xOc;,. :KOkXx.      l0d;;. .kO:;lOd. '0xc0X:  .xk. .dXkOXl .k0lxO, .kXxOK;           
           ,ooc.  .c'.'.'c. .::..;l.       ;:.'l.  .c'  .col'   .:,    .;ool;.   ,c. ;:. .:,  .c;..::.      ,c;. ,;   'ldl'   ,:. ;,   .;loc..;:..;c.       'loo'  .:ool;.  .:, .:.   ;;. .c;..::..;ol;.  'c,..:;           
                                                                                                                                                                                                                            
                      ...............     ................     ..............     .....................              .............................                       ..........................                         
                      .,,...........''    ,'.............,.   .,'..........,'     ''..................'.             ',...............................                ............................,.                        
                       .,.          .,.  .,.             ''   ''          .'.    .'.                  .'             ''                             ..'.            .'..                         .'.                        
                        '.           .,..,.              .,. .,.         .'.    .,.                   .'.            ''                                ''.         .'.                           .'.                        
                        .,.          .''''                .'.'.          ''     ''          ..         .,.           ''                                 .'.       .,.                            .'.                        
                         .'           .;,.                 ';'.         .,.    .,.          ''          ''           ''           .'...........         .,.       ''             .................,.                        
                         .,.           '.                  .,.         .'.    .'.          .,,.         .'.          ''           ''         ''          '.       ''            .,,................                         
                          .,.                                          .,.    .'          .,..,.         .,.         ''           ',.........'.         .,.       .,.            ..'.                                       
                           ''                                         .,.    .,.          '.  ''          '.         ''           ............          ''         .'.             .''.                                     
                           .,.                                        ''     ''          .'.  .,.         .,.        ''                               .'.           .'.              .'.                                    
                            .'.                  ..                  .,.    .,.         .,.    .,.         .'.       ''                            ..'..              .'.             .'.                                   
                             ''                 .;,.                .'.    .'.          .'......'.         .'.       ''                           ','.                 .',.            .,.                                  
                             .,.               .''''                .'     .'                               .,'.     ''           .'.              ........................             ''                                  
                              .'.              ''..,.              .,.    .,.                                ';'     ''           ';'..                                                 ''                                  
                              .'.             .,.  .'.             ''     '.                                 .',.    ''           '' .'..                                              .,.                                  
                               .,.           .'.    '.            .,.    .,.         .'..............          .'.   ''           ''   .'..                                           .,.                                   
                                ''           .'     .,.          .,.    .,.         .'.            .'           ''   ''           ''     .''.                                       .''.                                    
                                .,'..........,.      .'..........''     ',..........''             .''..........';.  ',...........,'       ...........................................                                      
                                 .............        ............      .............               ...............  ...............           ...................................                                          
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                  
""")
    largura_terminal = shutil.get_terminal_size().columns
    for linha in titulo.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def episodio():
    episodio = """                                                                                                                                                      
                                                                                                                                                      
         .:lc;;;c,      .,ll;,:c;.      .:o:.       .,;,,::.        .;;,,;:cc:'         'll:,,;:c:,.        .,ll:;;:;.               'll,             
         .xWk'..,'       cN0,.'xXx.     .xWd.      .oO;  .:.      'dx:.   .';xKk;       ,0Nl....;oO0d'       :XXc..',.               ;KX:             
         .dWx.           :X0'  ,K0,     .xWd       .kXo.         ,00;        .oNK:      '0N:      .xN0,      ;XK;                    ,KK;             
         .dW0c;;:.       :X0' .lk:      .xWd        'kNKx;      .xWk.         '0Wx.     '0N:       'OWd.     ;XNd;;:,                ,KK;             
         .dWO;.';.       :X0'..'.       .xWd         .;dXXx.    .xMO.         .OWd.     '0Nc       .kWo      ;XXl'';,                ,KK;             
         .dWx.           :X0'           .xWd            'kNl     ;KNl.        ;K0,      '0Nc       ;K0,      ;XK;                    ,KK;             
         .xWO'  .'.      cN0'           .kWd.      ;c.  .dO;      ,kKx;.    .;xd'       ,0No.   ..cxo'       :XXc. ...               ;KX;             
         .cdoc;;:;.     .;do'           .cdc.      'l:,,::.         ,clc;,,,;;.         ,odo:,',;;;.        .;odl:;::.               ,oo;.            
                                                                                                                                                      
                                                                                                                                                      
    """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in episodio.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def texto():
    texto = """
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
    largura_terminal = shutil.get_terminal_size().columns
    for linha in texto.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)
        time.sleep(1.5)



def centr(texto):
    largura_terminal = shutil.get_terminal_size().columns
    linha_centralizada = texto.center(largura_terminal)
    print(linha_centralizada)



def imperio():
    imperio = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxdocc::;;;;;::cldxO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWXOdc;..                    ..,cdOXWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMNOo;.      ..,;clo;   .:olc:,..      .;oONMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMNkc'     .;ldk0xolc:;.    ';:clok0Odl;.     'lONMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMWKo,    .;okXWMMMNc                cNMMMWXko,.    ,dXWMMMMMMMMMMMMM
    MMMMMMMMMMMW0c.   .;d0WMMMMWX0x;                ;x0XWMMMMW0o,    .lKWMMMMMMMMMMM
    MMMMMMMMMWKc.   .lONMMMMNOo:..                     .;oONWMMMNOc.   .oXMMMMMMMMMM
    MMMMMMMMNd.   .lk0NMMNOl'        .;cloooooolc,.        'lONMMXOkc.   'xNMMMMMMMM
    MMMMMMW0;   .ckd'.,dd,           ,KMMMMMMMMMMO.           ,do'.,xk;    cKMMMMMMM
    MMMMMWx.   'xk,                   oWMMMMMMMMNc                   :Od.   ,OWMMMMM
    MMMMNo.    ,:.        ..          '0MMMMMMMWx.          .         .c'    .xWMMMM
    MMMNl   .,.         .:OOc.         lNMMMMMMK;         'd0x,          ''   .xWMMM
    MMWo.  .o0,        ,kWMMW0c.       .kMMMMMWd        'dXMMMXo.        c0c   .kWMM
    MWk.   l0;        :KMMMMMWW0:.    ':OWMMMMNx;.    .oXMMMMMMWk.        l0:   '0MM
    MK;   ;Kx.       cXMMMMMMMMMWO:,lONWMMMMMMMMWXkc,oXMMMMMMMMMWO'      .,O0'   cNM
    Wd.  .xWNKO:    .kNWMMMMMMMMMMWWWMMMMMMMMMMMMMMWWWMMMMMMMMMWN0c     c0XWWd   .kM
    N:   ;KMWMNc     ..,:ldk0XWMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxoc;..      lNMWMK,   lW
    0'   lWMMM0'            ..,lKMMMMMMMMMMMMMMMMMMMMMM0:'.             ,KMMMWc   ;X
    k.  .xMMMMk.               ,KMMMMMMMMMMMMMMMMMMMMMMO.               .OMMMMo   '0
    x.  .xMMMMk.               ,KMMMMMMMMMMMMMMMMMMMMMMO.               .OMWMMd   .O
    k.  .xMMMMO.            .';oXMMMMMMMMMMMMMMMMMMMMMMKl;'.            ,KMMMWo   '0
    0'   lWMMMX;     .';coxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxoc;'.     cNMWMN:   ;X
    N:   ,KMWN0:    .kNWMMMMMMMMMMNNWMMMMMMMMMMMMMMNXWMMMMMMMMMMWNx.    cKNWMO.   oW
    Mx.   dNo..      cXMMMMMMMMMNx,.ckKWMMMMMMMMN0d;.:OWMMMMMMMMMK;      .'xNc   '0M
    MX:   .Ox.        cXMMMMMMXx,     .:0MMMMMWk,.    .:OWMMMMMW0;        'Od.   oWM
    MM0'   ,0d.        ;0WMMXd'        ;KMMMMMMO.       .:OWWWNx.        .kk.   :XMM
    MMWk.   ,l.         .oOd'         .kWMMMMMMWl         .:kk:          'c.   ;KMMM
    MMMWk.     ..                     cNMMMMMMMM0'                     '.     ;KMMMM
    MMMMWO'    cOl.                  '0MMMMMMMMMWd.                  .dO:    :KMMMMM
    MMMMMMK:    ,xk;..oko'           lNMMMMMMMMMW0,           ,xOl..cOx'   .dNMMMMMM
    MMMMMMMNx'   .:kOKWMMXk:.        .,:ccllllc:;'.        .cONMMWKOx,    ;OWMMMMMMM
    MMMMMMMMMKl.   .;kXMMMMWXkc,.                      .,lkXWMMMWXx,    'xNMMMMMMMMM
    MMMMMMMMMMWKl.    'o0NMMMMMNKko'                ,okKWMMMMWXkc.    'dXMMMMMMMMMMM
    MMMMMMMMMMMMWKo'    .,lkKWMMMMX:                cNMMMMNKxc'    .;xXMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMNkc'     .;lxOKKxc:;,'.    .',;:cxKKkdc,.    .,o0WMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMWNkl,.      .';:lood:   .cdool:;'.      .;o0NMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMWKxl;'.                        .':okXWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWNKkdoc:,'.........'';:loxOKWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXKKKXXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in imperio.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def escudos_lado_a_lado():
    imperio_lines = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxdocc::;;;;;::cldxO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWXOdc;..                    ..,cdOXWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMNOo;.      ..,;clo;   .:olc:,..      .;oONMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMNkc'     .;ldk0xolc:;.    ';:clok0Odl;.     'lONMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMWKo,    .;okXWMMMNc                cNMMMWXko,.    ,dXWMMMMMMMMMMMMM
    MMMMMMMMMMMW0c.   .;d0WMMMMWX0x;                ;x0XWMMMMW0o,    .lKWMMMMMMMMMMM
    MMMMMMMMMWKc.   .lONMMMMNOo:..                     .;oONWMMMNOc.   .oXMMMMMMMMMM
    MMMMMMMMNd.   .lk0NMMNOl'        .;cloooooolc,.        'lONMMXOkc.   'xNMMMMMMMM
    MMMMMMW0;   .ckd'.,dd,           ,KMMMMMMMMMMO.           ,do'.,xk;    cKMMMMMMM
    MMMMMWx.   'xk,                   oWMMMMMMMMNc                   :Od.   ,OWMMMMM
    MMMMNo.    ,:.        ..          '0MMMMMMMWx.          .         .c'    .xWMMMM
    MMMNl   .,.         .:OOc.         lNMMMMMMK;         'd0x,          ''   .xWMMM
    MMWo.  .o0,        ,kWMMW0c.       .kMMMMMWd        'dXMMMXo.        c0c   .kWMM
    MWk.   l0;        :KMMMMMWW0:.    ':OWMMMMNx;.    .oXMMMMMMWk.        l0:   '0MM
    MK;   ;Kx.       cXMMMMMMMMMWO:,lONWMMMMMMMMWXkc,oXMMMMMMMMMWO'      .,O0'   cNM
    Wd.  .xWNKO:    .kNWMMMMMMMMMMWWWMMMMMMMMMMMMMMWWWMMMMMMMMMWN0c     c0XWWd   .kM
    N:   ;KMWMNc     ..,:ldk0XWMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxoc;..      lNMWMK,   lW
    0'   lWMMM0'            ..,lKMMMMMMMMMMMMMMMMMMMMMM0:'.             ,KMMMWc   ;X
    k.  .xMMMMk.               ,KMMMMMMMMMMMMMMMMMMMMMMO.               .OMMMMo   '0
    x.  .xMMMMk.               ,KMMMMMMMMMMMMMMMMMMMMMMO.               .OMWMMd   .O
    k.  .xMMMMO.            .';oXMMMMMMMMMMMMMMMMMMMMMMKl;'.            ,KMMMWo   '0
    0'   lWMMMX;     .';coxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxoc;'.     cNMWMN:   ;X
    N:   ,KMWN0:    .kNWMMMMMMMMMMNNWMMMMMMMMMMMMMMNXWMMMMMMMMMMWNx.    cKNWMO.   oW
    Mx.   dNo..      cXMMMMMMMMMNx,.ckKWMMMMMMMMN0d;.:OWMMMMMMMMMK;      .'xNc   '0M
    MX:   .Ox.        cXMMMMMMXx,     .:0MMMMMWk,.    .:OWMMMMMW0;        'Od.   oWM
    MM0'   ,0d.        ;0WMMXd'        ;KMMMMMMO.       .:OWWWNx.        .kk.   :XMM
    MMWk.   ,l.         .oOd'         .kWMMMMMMWl         .:kk:          'c.   ;KMMM
    MMMWk.     ..                     cNMMMMMMMM0'                     '.     ;KMMMM
    MMMMWO'    cOl.                  '0MMMMMMMMMWd.                  .dO:    :KMMMMM
    MMMMMMK:    ,xk;..oko'           lNMMMMMMMMMW0,           ,xOl..cOx'   .dNMMMMMM
    MMMMMMMNx'   .:kOKWMMXk:.        .,:ccllllc:;'.        .cONMMWKOx,    ;OWMMMMMMM
    MMMMMMMMMKl.   .;kXMMMMWXkc,.                      .,lkXWMMMWXx,    'xNMMMMMMMMM
    MMMMMMMMMMWKl.    'o0NMMMMMNKko'                ,okKWMMMMWXkc.    'dXMMMMMMMMMMM
    MMMMMMMMMMMMWKo'    .,lkKWMMMMX:                cNMMMMNKxc'    .;xXMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMNkc'     .;lxOKKxc:;,'.    .',;:cxKKkdc,.    .,o0WMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMWNkl,.      .';:lood:   .cdool:;'.      .;o0NMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMWKxl;'.                        .':okXWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWNKkdoc:,'.........'';:loxOKWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXKKKXXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """.split("\n")

    resistencia_lines = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx'.;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl.   'dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo.       ,xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMMMMMMMMMWk.           ;KMMMMMMMMMMNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdd0WMMMMMMMMMM0,           cXMMMMMMMMMMNOdxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;'lKMMMMMMMXxd0WMO.         :XMNkoOWMMMMMMWO:'cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd' .xWMMMMMMNk,  .;kXl        .kXd,  .:0WMMMMMMXl..;kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMNx'  'OWMMMMMMNo.      cl.       ,d,      'kWMMMMMMNd.  ;OWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWO,   'OMMMMMMMMWKx:.                     'oOXWMMMMMMMWd.  .cKMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMNo.   .xWMMMMMMMMMMMWKc.                 'xNMMMMMMMMMMMMNl    'kWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMK:     cNMMMMMMMMMMMMMMWO,              .lXMMMMMMMMMMMMMMMK,    .dNMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMK;     .kMMMMMMMMMMMMMMMMMX:            .dWMMMMMMMMMMMMMMMMWo     .oNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMX:      ,KMMMMMMMMMMMMMMMMMMX;          .oWMMMMMMMMMMMMMMMMMMx.     .oWMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMNl       ;XMMMMMMMMMMMMMMMMMMMk.         :XMMMMMMMMMMMMMMMMMMMk.      .kMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMx.       ,KMMMMMMMMMMMMMMMMMMMNc        .xMMMMMMMMMMMMMMMMMMMMx.       ,KMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMX;        .kMMMMMMMMMMMMMMMMMMMMd        .OMMMMMMMMMMMMMMMMMMMWl         oWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMk.         lNMMMMMMMMMMMMMMMMMMMd        '0MMMMMMMMMMMMMMMMMMM0'         ;XMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWl          .xWMMMMMMMMMMMMMMMMMWo        .kMMMMMMMMMMMMMMMMMMNc          .kMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMN:           .OWMMMMMMMMMMMMMMMMX;         oWMMMMMMMMMMMMMMMMNo.          .dMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMX;            .xNMMMMMMMMMMMMMMWd.         '0MMMMMMMMMMMMMMMXc             dMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMX:              :OWMMMMMMMMMMMWx.           ,0MMMMMMMMMMMMNx'              dMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMWc               .;xKWMMMMMMWOc.             .oKWMMMMMWNOo'               .kMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMd                  .,:loooc,.                 .;coooc;.                  ,KMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMM0'                                                                       lWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMNl                                                                      .OMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMM0'                                                                     oWMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMWx.                                                                   :XMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMWd.                                                                 ,KMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWd.                                                               ;KMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWk'                                                             :KMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMK:                                                          .dNMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMNx'                                                       :0WMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMXo.                                                   ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd'                                              .;kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;.                                         .lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;.                                   'ckXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl;.                          .':oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOxo:,'..           ..';cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0OOkkkkkOO0KXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """.split("\n")

    for lines in [imperio_lines, resistencia_lines]:
        while lines and lines[0].strip() == "":
            lines.pop(0)
        while lines and lines[-1].strip() == "":
            lines.pop()

    separador = "   "

    largura_imperio = max(len(l) for l in imperio_lines)
    largura_resistencia = max(len(l) for l in resistencia_lines)
    largura_total = largura_imperio + len(separador) + largura_resistencia

    cols_terminal = shutil.get_terminal_size().columns
    recuo = max(0, (cols_terminal - largura_total) // 2)
    margem = " " * recuo

    num_linhas = max(len(imperio_lines), len(resistencia_lines))
    imperio_lines += [""] * (num_linhas - len(imperio_lines))
    resistencia_lines += [""] * (num_linhas - len(resistencia_lines))

    for imp, res in zip(imperio_lines, resistencia_lines):
        print(margem + imp.ljust(largura_imperio) + separador + res)



def dentro_da_nave_resistencia():
    dentro = """
        .......................................,,,,,,,,,'............................................................          ....................     ..,,,,,,,,,.............................................
        .....................................',,,,,,,,'.............................................................          ....................        ..',,,,,,,'...........................................
        ..................................',,,,,,,,'...............................................................          ...................            ..',,,,,,,,'... ....................................
        ...............................',,,,,,,,'................................................................          ...................                 ..',,,,,,,,......................................
        ............................',,,,,,,,'..........................            ............................          ..........;l;.....                     ...,,,,,,,,'...................................
        ..........................',,,,,,,'.....................            ..............  ..................          ..........,oxc'..                           ..',,,,,,,,'................................
        .......................',,,,,,,'....................     .............................................         .........'lxl'..                                ..',,,,,,,'..............................
        ....................',,,,,,,'......................  ..............................................          .........'cdl'..                                    ..',,,,,,,,'...........................
        ..................',,,,,,'''....................... .....'.................................'.......        ..........cdl,..                                         ..',,,,,,,,'........................
        ...............',,,,,,'''..............................;do'................................;oc'....      ..........:do,..                                             ...,,,,,,,,'......................
        ............'',,,,,'''.................................:xOl................................l0x,....... ...........,c;..                                                  ..',,,,,,,,'...................
        ..........',,,,,'''.....................................'::,';:;,.....................';:,,cc'.......................                                                       ..,,,,,,,,,.................
        .........,,,,''...........'..................................,;::'..':::::,...;::::'.'::;'...........................               ..  .                                     ..',;,,,,,,'..............
        ........,,,,'.........''',,,,'''.....................................',,;;'....'............................'''.......              ......                                       ..,,,,,,,,,'...........
        .......,,,,'........',,,,,,,,,,,,'''.................................''''.................................''...''.......            ......                                         ..',,,,,,,,'.........
        ......,,,,'.......'',,,,,,,,,,,,,,,,,,''..........................'''''.................................'''..  ..''......            .          ..  ..                                ..',,,,,,,,'......
        .....,,,,'.......',,,,,,,,,,,,,,,,,,,,,,,,''....................''''...................................''..... ...''.......                     ......                                  ..',,,,,,,,'....
        ....',,,'.......',,,,,,'.'''',,,,,,,,,,,,,,,''...............'','...................................''''............''......                    ......                                     ..',,,,,,,,'.
        ...',,,'.......',,,,,'...........''',,,,,,,,,,'............',''......................................',,'............'''......                  ..  ..                ..                      ..,,,,,,,,
        ...',,,'......',,,,,'...:dxdlc:,'.......'',,,,'.........'','''........................................,::;.............''......                                      .,.               ..........',,,,,,
        ...',,,'.....',,,,'...;xxc:clddxdxxdol:;'..',,,'......'''''''''''''''''''''''''''''''''''''''..........';::'............'''......                                             ..........'',,;;::ccllc;,,
        ...''','.....',,,...'oOo'........';:cloxkl..',,'.....''''''''''''''''''''''''''''''''''''''''''..........,::;.............,'......                                    .........',,;::clloddxxxxxxxxxxdl:
        ...''','.....',,'..,kx,............... .c0l..','....'''''',,,,,,,,,,,,,,,,'''''''''''''''''''''''..........;::,............','......                           ........',;;:cllodxxxxxxxxxxxxxxxxddddddo
        ...''','.....',,'..l0:.......''....''.. .c0l..,'....'''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''.........'::;'............''.......                   .......',;::clodxxxxxxxxxxxxxxxxxdddddooooooooo
        ...',','.....',,,..l0;....',;;'...''''.. .xO,.''........',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''.......,::,............'''......            .......',;:clodxxxxxxxxxxxxxxxxxxdddooooooooooooooooo
        ...',','.....',,,..l0:....;;;;'..'''''.. .d0,.''. . . .',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''......';:;'............''......      ......',;:clodxxxxxxxxxxxxxxxxxxxxxxddoooooooooooooooooooo
        ...',,,'.....',,,..l0:....;;;;'..'''''.. .d0,.''.   ..,,,',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',''''''''.......,::,. . ........'''...........',;:lodxxxxxxxxxxxxxxxxxxxxxxxxxddddooooooooooooooooooooo
        ...',','.....',,,..l0:....;;;;'..'''''.. .d0,.''.....;:;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'',,,'''''''.......;,. . ..........''.......,clodxxxxxxxxxxxxxxxxxxxxxxxxxddoooooooooooooooooooooooooooo
        ...','''.....',,,..l0:....;;;;'.....''.. .d0,.'.. ...',,',,,,,,,,,,,,,,,,,,,,,,''''',,,,,,,,,,,,''',,,''''''......... ..............'''.....'lxxxxxxxxxxxxxxxxxxxddooooooooooooooooooooooooooooooooooooo
        ...','''.....',,,..l0:....;;;;'......'.. .dO'...     ...'',,,',,,,,,,,,,,,,,,,,,'''''''''',,,,','','''''''..''...................';:lc,'......;dxxxxxxxxxxxxddoooooooooooooooooooooooooooooooooooooooooo
        ...'''''.....',,,..l0;....,;;,'......... .c:            ..',',,,,,,,,,,,,,,,,,,,,,,,'''''',,,,'''',''''''.....................';codxxxl;''.....'lxxxxxxdddoooooooooooooooooooooooooooooooooooooooooooooo
        ...'''''.....',,,..l0; ...,,,,.......... .,.           ....'''''''''''''''''''''''''''''''''''''''''''''''.....................'''',,,,,'''......,:clllllllllooooooooooooooooooooooooooooooooooooooooooo
        ...''','.....',,,..l0; ...,,,,.......... ...           .....''.''''..''''........''''''''''''''''''''''''''............................''''''................'''',,,;;;;:::ccclllloooooooooooooooooooooo
        ...'''''.....',,,..l0; ...,,,,.........  ..            ......''..'..................'''''''''''''''''''''.............   .........................''''''...........................''',,,;;;:::ccclllloo
        ...'''''.....',,,..l0c................  'l,             ...';;;;;;;;;;;;;;;;;;,,,,,,,'''.............................      ...............;l:.................''''''''''..............................''
        ...'''''.....',,'..,kO;............'''''cl.            .....,,,,,,,,,,,;;;;;;;;;;;;;;:::;;;,,,''...............            ......:lolc:;'',:,.............................'''''''''''''''...............
        ...'''''.....',,,...'d0l.....',,;::::::;;,..              ..........................'''',,;;;::cc:;,,,'.............        ......',:cloddd:.......................  .................''''''''''''''''''
        ...'''''.....',,,,'...cOo,,;;:ccc:;,'''......           ....................................'',;ccc::::;,'...........            .........'.........................  ... ..  ..................''''''''
        ....'''''.....',,,,'...;lccccccccc;,''........    .........................................'',;:cccccccc:,...........       ...         ............................         .......           .........
        .....''''''.....',,,,....,;::ccccccc::;;;,,,'.................................'''''',,,,;;;::ccccccc:::;'............      ........           ................................. .       . .:ddl:. ...   
        ......''''''.....'''''......',;;:::ccccccccc;............,;;;;;;;;;;;;;;;;;;:::::::cccccccccc:::;;,'''...............      ...............           .................................    .:odd;....... 
        ........'''''........''.....''....',,,;;;;::;............,:::cccccccc:::::::;;;;;:::::;;;;,,''....';:,...............  ..  ....................            ............................;:,'..    .......
        .........''..........'''....;cccc:;,'......................................................,;::ccccc:,...............  ..  .........................              ...................,d0KK0Oxdlc:,'...  
        .....................'''.......';:ccccc,..................................................,cc:;,..........................................................             ................,;:lodk0KKK0Oxdoc
        ..........................................................                    ................................................................................                ................',:cldxO0K
        ......................''',,,;,,'.. .......................                   ....................''''''''..........................................................                  .................';
        ...................',,,;;;;;;,,;,....       ......................................           ....,,,,,,,,,,,'''''.......................................................                    ............
        ..............''',,,;;;;;;;;;,,,'....       ...... .......              ......               ....',,,,,,,,,,,,,,,,,,''''.......................................................                  .......
        .........''',,,,,,,,;;,,,,,,,''......       ...... ......              .......               ..........'''',,,,,,,,,,,,,,,,,,,''''''................................................                    
        ....'',,,,,,,,,,,,,,;,,,''...........       .....  ......              .......               ..................''''',,,,,,,,,,,,,,,,,,,'''''..............................................              
        ',,,,,,,,,,,,,,,,,,,''...............      ......  ......             ........               ...........................'''',,,,,,,,,,,,,,,,,,,'''''...........................................         
        ,,,,,,,,,,,,,,,,''...................      .....   ......             ........                ................................'''',,,,,,,,,,,,,,,,,,,,,,'''''.......................................    
        ,,,,,,,,,,,,''......................       .....   ......             ........         ..     .......................................''''',,,,,,,,,,,,,,,,,,,,,,,'''''..................................
        ,,,,,,,''.......................................  ......              ......... ..............................................................'''',,,,,,,,,,,,,,,,,,,,,,,'''''..........................
        ,,,''....................................................         ..   ...............................................................................'''',,,,,,,,,,,,,,,,,,,,,,,,''....................
        '..........................................      .......  ....................................................................................................'''',,,,,,,,,,,,,,,,,,,,,'................
        ...........................................     ..        ..........................................................................................................''',,,;,,,,,,,,,,,,,,,'.............
    """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in dentro.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def imagem_texto_batalha():
    texto = """                                                                             
          ..............       ........   ................   ..........     ......       ......   ......    .........             
         .,'............'.    ''......',..,..............,. ',........,.   .;...,'      .,...,'  .,'...,.  .,.......,.            
         .,.   ......   .,.  .'   .'   ''.,'....    .....,..,.  .;'   .'   .'   .'      .'   .'  .,.  .'.  ,.  .'.  .,.           
         .,.   .'..'.   .'. .'.  .;:.  .,. ....,.  .,'.....'.   ,::.   '.  .'   .'      .'   ......   .,. .'   .:,   ',           
         .,.    ....   .;'  ''   ,;,;.  .'     '.  .,.    .'   ';.';.  .'. .'   .'      .'            .,..,.  .;';'   '.          
         .,.   ',...'.   ''.'    ....    ''    '.  .,.   .,.   ......   '' .'   .,......''   .......  .'.'.   .....   .,.         
         .'.   ......    .;,.   ......   .,.   '.  .,.   '.   .......   .,..'    ......'c,   .'  .,.  .,;'   .......   .'         
         .,'.............';;...',....',...,,   ,,...;.  ';...',.   .',...,,',..........'c:...,'  .,,...cl'...,'.  .,....;.        
          ..............  ......      ......   ......   ......       ..........................   ............     .......        
                                                                                
    """
    pygame.mixer.init()
    pygame.mixer.music.load('Star-Wars-Imperial-March.ogg') 
    pygame.mixer.music.play()

    largura_terminal = shutil.get_terminal_size().columns
    for linha in texto.split('\n'):
        linha_centralizada = linha.center(largura_terminal)
        for c in linha_centralizada:
            print(c, end='', flush=True)
            time.sleep(0.009)
        print()
    pygame.mixer.music.stop()



def esploção_das_naves():
    esploção = """
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMWWWMMMWWWMMWWWMMWWWMMMWWMMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWWWMWWWMMMWWMMMWWMMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWWWMWWMMMWWWMMWWWMMMWWWMMWWWMMWWWWMMMWWMWNWWWMMWWWMMMWWMMMWWWMMWWWMNNWWWMMWWMMMWWWMMWWWMMMWWMMMWWWMMWW
        WMMWWMWWWWMMWWWMMMWWMMMWWWWMMWWWWMMWWWWNKXWWWWWMWWWWMMWWWWMMMWWWWWWWWWWWMWWMWMX0NMMWMMWWWWWWWWMWWWMMWMWWWWWWWWWWWWMMMWWWMWWWWWWMMWMWWWWMWWWM
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWXOOXWWWWMMWWWMMWWWMWKKWMMMWWMMMWWWX0kxkk0NWWWMMMWWWMMWWWMMMWWMMMWWWWMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMWWWMMN0k0WMWWWMMWWWMMMWWXXWWWWMMWNNNXxc;,,,,;cxXMWWWMMMWWMMMWWWNNWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMWWWWWWWWWMMWWWWKkONWWMWWWMMWWWWN0KWMMMNkolcl:,,,,,,,,,;oOXWMWWWMMMWWWWX0XWMMWWWWWWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMM
        MWWWWWMMWMMWWMWMMMWWWWMMWWMWWMNKNWWWWWMWWWWWN0OXWMWWWWWWWMXo'lXMWKc.',,,,,,,,,,,,,,,;:kNMWMMWWWWN0kKWWMMWWMWNNWWMWWWWWWWWWMMMMMMWWWWWMMMWWWM
        WWMMMWWWMMWWWMMWWWMMMWWWMWWWWMWK0O0KXWWWMMWWWWXXWNKNWWWMMMWOd0WMNl..',,,,,,,,,,,,,,,,,;OMMWWWWWXkkKWWWWWMMMWWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMXxl;,,,;:oOKKKNWWWWMMWWWWMWXOxxkOXWXd,....''',,,,,,,,,,,,,:0WWNXNWKxkXWMMMMMMMMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMM
        WWMMWWWMMMWWWMMMWWMMMWWWKkxdc,,,,,,,,,,;;;coONMN0xdddkxc;;;;;cxo,,,,'....',,,,,,,,,,,;oXWWNXXOxkXWMMMMWWMMMWWWMX0NMMMWWWMMWWWMMMWWMMMWWWMMWW
        WWMMWWWMMMWWWMMMWWMMWWXd;,,,,,,,,,,,,,,,,,,,;dOo;;;;;;;;;;;;;;;;;;;;;,''',;;,,,,,,,,,;;cxNN0xdxKWMMMWWWMWWWMWWMXKWWMWWWWMWWWWMMMWWMWWMMWMMWW
        MMWWWMMWWWMMMWWMMMWWWNo,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:cc:;,,,,,,,,,.'okddx0NNNWWWWMMWWMMMMWWMMWWWWWWWWMMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMMWWMMWk,',,,,,,,,,,'''',,''',;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;ccc;;,,,,,,,'..:ddx0WWNNWMMWWWMMWWWMMMWWWMMWKXMMWWWMMMWWMMMWWMMMWW
        MMWWWMMWWWMMMWWMMMWWWd..,,,,,,,''........'',,;;;;;;;;;;;;;;;;;;;;;;;;::::ccccc;,,,,,'...;odd0WWWMMWWWMMMWKXMMWNXWWMWWMMMWWMMMWWWMMWWWMMWWWMM
        MMWWWWWMWWMMMWWMWWWWMO,..''',,'.........,,;;;;;;;;;;;;;;;;;;;:cc:;:ccccccccccc;'........,cdONWWWWWMMWWMWWWWWMKc;l0WWWWWMWWMMMWWWMMWWMMMWWWMM
        WWMMMWWMMMWWMMMMWWMMMWk;..............',;;;;;;;;;;;;;;;;;;;;;;:cccccllllllllcc:;;,,'''...,xNWWWWWWWMMWWWWWWWNo..'kWMWWWWMMWWWMMMWWMMMWWWMMWW
        MMWWWMMMWWMWNNWWMWWWWMMXxl;'..........';;;;;;;;;;;;;;;;;;;;;;::cccloddddddddlccccc:;::;;::lxxollxKWWWWWWX0NMW0xx0NWWWMMWWWWNKXWWMMWWWMMMWWMM
        WWMMWWWMMMWWNXXKKXWMWWWMMW0;..........',;;;;;;;;;,'.,;;;::;;:ccccldddddddddddlcccccccccccccc:;,,,c0WWNXXNWWWWMMMWWMMMWWWMNK0KNWMWWMMMWWMMMWW
        WWWMWWWMMWMWWWWNXXNWWWMMWMO,...........',;;;;;;;;;,',;::cccccllllodddddddddddocccccccccccccccc;,,,okoc:cldKNKkxdxk0NWWWWWNNWMWWWWWMMMWWMMMWW
        MMWWWMMMWWMMWWWWMMWWMMMMWWXc...........',;;;;;;;;;;:cccccccclddddddddddddddddollllcccccccccccc:;,,'..',,,,:c;,,,,,;ckNMMWWWMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMWWWMMMN0kKWWXo,.........,;;;;;;;;;;cccccclooooodddddddddddddddddddooloooooccccc:,,'....',,,,,,,,,,,,,;xNMMMWWWMMWWWMMMWWWMMWW
        MMWWWMMWWWMMMWWWMMWWWx;';oKMWKxocc,....,;;;;;;;;;ccccccloddddoodddddddddolcccldddddddddddocccc:,'.....',;,,,,,,,,,,,,cONWWWMMWWMMMWWWMMMWWMM
        MMWWWWWWWWMMWWWMWWWWWk:;,lKMWWWKkd:....,;;;;;;;;:cccccloddddddddddddddol:;;;;:cloddddddddolcc:;,'''...,;:;;;;,,,,,,,,,;cxKWWMWWWMMWWWMMWWWMM
        WWMMMWWMMMWWWMMWWWMMMNXKKXWWWKl,......';::::;;;;ccccccloddddxxdddddddddoc:;::::;codddddddoccc:::cc;'',;;;;::;;;;;;,,,,,,,lKWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMK:........,;::::;;;;:cccccloddddxOOxdddddddddlclllloodddoddddollcccccc:;;;;;;:;;:::;;;;,,,,,,;kMMWWWMMWWWMMMWWMM
        WWMMWWWWMMWWWMMMWWMMMWWMMWMWd.........';::::::;,,,;:cccodddddxkkxxxxdddddddddddddddxxddddolcccccccccc:;;;:::::;;;:;,,,,,,:OMWMMWWWMMMWWWMMWW
        WWMMWWWMMWWWWWMMWWMMMWWMMMMWo..........',;:::::;::::cclloddddddx0KK0kkxxxdxxxdddddxxxdddolccccccccc:;,,,,;;:::::;;;,,,,,;kNWWXXWWWMMWWWWMMWW
        MMWWWMMWWWMMMNNWMMWWWMMWWWMM0;............',;:cccccclodddddddddkKXXXXKKK0kOKOkkO0Okxddddooolccccc:;,,,,,,,,;;;;;;,,,,,,,;kWMWXXWMMWWWMMWWWMM
        WWMMMWWMMMWWWXKNWWMMMWWMMWWWW0c'............;cccccclddddddddddk0XXXXXXXXXXXXXXXXXXKkdddddddocccc:,,,,,,,,,,,,,,,,,,,,,,,,oNWWMMMWWWMMWWWMMWW
        MMWWWMMWWWWMWWWMMMWWWMMWK0WMMWN0xoo:'......':ccccccoddddddddddkKXXXXXXXXXXXXXXXXXXKkxxdddddoolcc:;,,,,,,,,,,,,,,,,,,,,,,,xWMMWWMMMWWWMMWWWMM
        MMWWMMWWWWMWWWWMMWWWWWMMWWWMMWWMMWNN0xo,..,:cccccccoddddddddxkOKXXXXXXXXXXXXXXXXXXXK0Oxdddddddolccc;,,,,,',,,,,,,,,,,,,;dXMWMWWMMNKXWMWWWWMM
        WWMMMWWMMMWWWMMWWWMWXKWMMMWWMMMMW0o0MWW0c,';ccccccclodddddddx0KXXXXXXXXXXXXXXXXXXXXKOxdddddddddlcccc;,,'..'',,,,,,,,,;o0WMMWWMMMNxckWWWWMMWW
        MMWWWMMWWWMMMWWMMMMXo:okKWMMMWWMMWXNWMMWXklcccccccccclooddddxxxkO00KXXXXXXXXXXXXXXX0kdddddxdddoccccc;,,,'..';lxxdoodkKWMWWMMMWWWWXKNWMMWWWMM
        WWMMMWWMMMWWWMMMWWMWk;,,cKMWMMMWWWWWWWN0dlcccccccccccccodxxddddddxdxxO0KXXXXXXXXXXXXKkdddooollccccc:;,,;;',cOWMMWWWMMMW0ONMWWWMMWWMMMWWWMMWW
        WWWMWWWWMMWWWMMMMWMMN0xxOXMWWMMMMWWWWNOlccccc::;;:cccccooolllloddddddxO0XXXXXXXXXXXK0kddolcccccccc:;,,,,,,,,oXMWWWMWWMNO0WMWWWWMWWWMMWWWWMWW
        MMWWWMMWWWMMMWWMWWWWWMMMWMMMWWWMMMWWWXdcccc:;,,,,:cccccc:::::ccllloddddkKXXXXXXXXXOddddolccccccccc:,',,,,,,':KMWXKXWWMMMWWWMX0NMMMWWWMMWWWMM
        WWMMMWWWMMWWWMMWXKWMMWWMMMWWWMMWWNWMWXdccc:,,,,,,:cccc:;;;;;;;:ccldddddOKKKXX0kO0Odlllolcccc:ccccc:;,,,,,,,:kWWO;'cKMWWWMMWWWWWMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWMMMWWWMMWWWMW00WMWKdlc:,,,,,,;:::;;;;;;;;;;:cldddddxkxxkkxdddddlccccc:;;,,;;;,,:cc:;,,:kWWWKdoxXMMMMWWWMMWWMMMWWWMMMWWMM
        WWWWWWWWWWWMWWMMMMWWMMWWMMWWMWWMWWWWWXOo:;;,',,,,,,,,,,,,,,,,,;:clodddddddddddddddlcccccc;,,;;,,,,,,;lolcccdXWWWMWWWWWWMWWWMMWWMMWWWWMMWWWMM
        WWMMMWWMMMWWWMMWWWWMMWWMMWKKWMMWWWMWOc,''''''..',,,,,,,,,,,,,,,;:cclddddddddddoolcccccccc;,,,;;,,,,,,:loooooONWWWWWMMWWWMMMWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWWWWMMWWMMMW0:''''''....,,,,,,,,,,,,,,,,,,;cldxdddddddlccccccccc:;,,,,,,,,,,,,:oxdodddOXWMMWWWWMMWXNMMWWWMMWWWMMMWWMM
        WWMMWWWMMMMWWMMWWMMMMWWMMMWWWMMWWWMk,'''''....',,,,,,,,,,,,,,,,,,,:lodddddddlcccccc::;;,,,,,,,,,,,,,,cKWXKK0kddOKNWMWWWWWXNWWMMMWWMMMWWMMMWW
        WWMMWWWMMMWMMWKdOWMMWMWWWMWWWMWWNNWXo,',''.....',,,,,,,,,,,,,,,,,,:ccllooollccc:::;,,,,,,,,,,,,,,,,,:OWMWWK0NX0kxkKNWWWWWMMWWWMMWWMMWWWMMMWW
        MMWWWMMWWWMMMWX0XWWWWMMWWWMMWX0O0XWWXkl;,,......'',,,,'..'''',,,,,,;:cccc::cc:,,,,,,,,,,,,,,,,,,,:okXWMMWWXXWWWNKOkkKNMMWWMMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMMWWMMMWWMMWNXOkk0NWMMMWNXOc...................'',,,,',;;;'..''''',,,,,,,,,,,,,,,,c0WMMWWWMMWWWWMWMWNKOOKNMMWWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWN0O0KXWWMMWWMMWM0;.....................'''''...........',,,,,,,,,,,,,,,,cKWWWWWNXXKXWMWWMMWWWNKKNWMMMWWMMMWWWMMMWWMM
        MMWWWMMWWWWWWWWMWMWWWWXKKKNWWWWMWWWMMMWMXl.....................................',,,,,,,,,,,,,,,,cKMWWNx;,,':0MWWWWWWWWWWWWMMMWWMMMWWWMMWWWMM
        WWMMMWWMMMWWWMMWWWMMWNNWWMWWMMMWWWMMMWWMMNxc,'..',cl;.......................',cxkl;,,;c;,,,,,,;l0WWMNo.....'kWMMWWWKKWWWMMWWWMMMWWMMMWWWMMMW
        MMWWWMMWWWMMMWWMMMWWWMMWWWX00NWMMMWWWMMWWWMWX0O0KXWWXkdlllo:...............;kXNWMWX00KNKOxdxxkKNMMWWNo...,oONWWWMMWKKWMMWWMMMWWWMMWWWMMMWWMM
        WWMMWWWMMMWWWMMMWWMMMWWMMW0dxXMWWWMMWWWMMWWWWMMWWWMMWWWWMMWx...............oNMMMMWWMMWWWMMMWWMMMWWWMW0ddxKWWWMMMWWWMMWWWMMWWWMMMWWMMMWWWMMWW
        WWWMWWWWMMWWWMMMMWWWWWWMMMWWWMMMWWWWWWWMMWWWWWMMWWMMWWWWWWMKc............,dXMWMNKNMWMMWWMMWWMMMWWWWWMMMMWWWWWMMMMWWMMMWWMMMWWMMMWWMMMWWWMMWW
        MMWWWMMWWWMMMWWMMMWWWMMWWWMMWWWMMMWWMMMWWWMMMWWMMMWWWMMWWWMMXxc::lxkxdddkKWMMWWWNWMWWWMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMM
        WWMMMWWMMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWMMMWWWMMWWWMMMWWMMWNNWMMMWWWMMMWWMMMWWWOoONWMMMWWMMMWWWMMWWWMMWWWMMMWWMMMWWWMMWWWMMMWWMMMWWMMMWW
        MMWWMMMWWWMMMWWMMMWWWMMMWWMMMWWMMWWWWMMWWWMMWWWMMMWWMMMWWMMMWWWWMWWWMMMMWNWWWMWWMMXd:oXMWWMMMMWWMMMWWMMMWWMMMWWWMMWWMMMWWWMMMWWWMMWWWMMMWWMM
    """
    pygame.mixer.music.pause()
    pygame.mixer.init()
    som_explosao = pygame.mixer.Sound("explosao.ogg")
    som_explosao.set_volume(1)
    som_explosao.play()
    largura_terminal = shutil.get_terminal_size().columns
    for linha in esploção.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)
    pygame.mixer.music.unpause()
    time.sleep(3)



def comandante_imperial():
    comandante = """ 
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
        ........................................................''............................................................................................'...........................................................
        .......................................................'''''''..................................................................................''''''''..........................................................
        .....................................................'''''''''''''...........................................................................'''''''''''''........................................................
        .......................................................''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.........................................................
        .................................''''.......................'''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''........................'''''..................................
        ....................... .........''''............................'''''''''''''''''''''''',,,,,,,'''''''''''''''',,,,,,,'''''''''''''''''',,''''.............................''''.........  .......................
        .....................  ..........'''.            .....''''''''''''''',..             ....',,,,'..    .. ..    ..',,,,,'.....    .  .   ..',,,''''''''''''.....             ..'''.........   ......................
        ....................    ........'''..            .....'''''''',,',,',,.                ..',,,,'.                .',,,,'..                .,,,,,',,,,''''''....              .''''.........   .....................
        ................'..    ........''''.            .....''''.....''''',,,.               ..',,,,'.                  .',,,,'..               .,','''''.....''''.....             .''''........    ....................
        ............'..'..    .........'''.            ....''''..     ....',,,.               .'',,,'.                   ..,,,,'..               .,','....     .''''.....            ..'''.........    ...................
        ...........'.''..    .........'''..          .....''''.        ...'',,.              ..',,,'.                     .',,,,'..              .,,,'...       ..',''....            .''''........     ..................
        ..........''''..     ........''''.          .....''''.         ...'',,.             ..',,,'..                      .',,,,'..             .,','...         .',''.....           .''''........     .................
        .........''''..     ........''''.          ....''',..          ...'',,.            ..',,,,'.                        .',,,'..             .,','...          .',''.....          ..'''.........     ................
        ........''''..     .........'''.         .....''''.            ..'',,,.            .',,,,'.                          .',,,'..            .,'''...           .',''.....          .''''........      ...............
        .......''''..      ........'''..        .....''''.             ..'',,,.           ..',,,'.           ......          ..,,,,'..           .,'''...            ..''''....          .'''.........      ..............
        ......''''..      ........''''.        .....''''.              ...',,,.          ..',,,'.           ........          .',,,,'.           .,'''...              .''''.....        ..'''........       .............
        ....'''''.       ........''''.       .....'''''.              ....',,,..        ..'',,,'.           ........          ..,,,,'...        .','''....             ..,,''......       .''''........       ............
        ...''''''...............'''''............'''',,'''''''''''''''''''''',,''''''''''''',,,,,'............................',,,,,,'''''''''''',,,,'''''''''''''''''''','''''............'''''................'.........
        ..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,''''''''''''''''''''..............'''''''''''''''''''',''''''''''''''''''''''''''.'''''''''''''''''''''''''''''''''''''''''''........
        .'''''.''''',,'..........',,.......',,',;'....','..';:;'''',''''''',,..',;;:;'...................................................';::;;,'.''''''''''''''''''.',''''..',;'',,..','...,;'..........','''.....''.....
        ''''''''...',;'.';cc:,..'';;'''''.......',...........'.......'...................................................................................................''..',.......'''.',;,'..';:;;,.';;,''............
        ''''.............''''.......................................';'..................................................................................,,........................................'''...'................
        ''...............',.........................................,;...................................................................................';.........................................',....................
        '................:;........................................................'''''''''''''''''''....................'''''''''''''''''''........................................................:,...................
        '................'.........................''',,,;;;;;;;;;,,,,,''''''''''',,,;;;;:::::ccccccll;.....  ....  .....;ccccccc:::::;;;;,,,''''''',,,,,,,,;;;;;;;;;;,,,,'''........................''.................''
        ''.......................................'',,;;::::ccccllllcccc:::;;,,,,''''..........'''',,,,,....           ...',,,''''........''''',,,,;;;:::ccccllllcccc::::;;;,,''''''...................................''''
        ''''.....................................................'..''........................''''''''''................'''''''''........................'''.....................'''''..'''..........................'''''
        ''''''...............................................................................''''''''''''..............''''''''''''...............................................................................''''''''
        '''''''.........................................................,.            ......'''''''''''''..............'''''''''''''......      .    .''.........................................................'''''''..
        ..'............................................... ... ....  . ...   ....   ......'''''''''''''''..............''''''''''''''......   .....   ....   ... ...  ...............................................''...
        .....................................,....  ...... ... ....  . ...  .....  ......''''''''''''''''..............'''''''''''''''....... .....   ....   ... ...  .....  ....'........................................
        .................................. .',..,.  ...... ... ... ... .,. ... .........'''''''''''''''''........ .....''''''''''''''''...........   .,. ... ... ...  .....  .,..'..  ....................................
        ...........................  ..... .,;....  ...... .,. ... ... .'.  .  ........''''''''''''''''''..............'''''''''''''''''........     .'. ....... .,'  .....  ... ',. ......  ...''........................
        .................. .,'.....  ..... .......  ...... .,. .    ...................''''''''''''''''''......'.......''''''''''''''''''................... . . .'.  .....  .......  .....  .'..','. ....................
        .........,.. ..... .;:.....  .....   ....   ...... .,.      .................''''''''''''''''''''......'.......'''''''''''''''''.'..................     .,'  .....   ......  ....  .....';.  ....  .'............
        ......'.',.  ..... ........  ..... .,,....  ...... ..       .;'...........................''''''.......'.........''''''''''''''''........... ....;'      ... ......  ... .,. .....  ........  ....  .,;''.........
        ... .::.,;.  ..... .'......  ..... ... .,.  ..,l:....       ......................................   ..'...   ....'''.....''''...................'.         ..,c;... .,. ... .....  .......'. ....  .,:.,c' ......
        ... .,,....  ..... ........  ..... .......  . .;l;...          ...................................   ......   .....................................        ..'lc...  ... ... ......  ........ ....  .....;. ..... 
        ..  ........ ..... .....''.  ...... .,'''.     ...................................................   ......   ..................................................     .''.,'. ......  ',.....  ....   ......  .... 
        .....''.'... ...........,'.  ........,....      ..................................................   ......   ..................................................     ....,'.......  .,,...... ....   .'..,. ..... 
        ..  .;'..'.  ..... ...'..... ....'.....                      .....................................   ....'..  .....................................           .          .........   ...'.... ....  .....;'  .... 
        ................'...........  . ......          .           .....................................    .......   .....................................          ..         ...... ..  ..............  ..............
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
        ..................................................................................................................................................................................................................
    """
    largura_terminal = shutil.get_terminal_size().columns
    for linha in comandante.split('\n'):
        # Centraliza a linha de acordo com o tamanho do terminal
        linha_centralizada = linha.center(largura_terminal)
        print(linha_centralizada)



def imagem_fim():
    texto = """                                                                                                                        
                              .'.................'. .'....'..  .'......'.        .'.....'.                              
                             .;.                .;..;.    .;;. .;.     .,.     .,'.     ',                              
                             .,.                .;..,.    .,:. .,        ,'   .,.       .,                              
                             .,.    .,,..........'..,.    .,;. .,         ',..,.        .,                              
                             .,.    .,,......'.    .,.    .,:. .,          .;;.         .,                              
                             .,.             ,'    .,.    .,:. .,           .           .,                              
                             .,.     .'......,.    .,.    .,:. .,     .;.        ,'     .,                              
                             .,.    .;.            .,.    .,:. .,     .:c.     .,c,     .,                              
                             .,.    .,.            .,.    .,:. .,     .,.',   .,.''     .,                              
                             .,.    .,.            .,.    .,:. .,     .,. ',..,. ''     .,                              
                             .;'....,;.            .;,....';,. .;'....,;.  .;,.  .;.....,,                              
                              ........              ........    ........          .......                               
                                                                                                                        
    """
    pygame.mixer.init()
    pygame.mixer.music.load('Star-Wars-Main-Theme-_Full_.ogg') 
    pygame.mixer.music.play()

    largura_terminal = shutil.get_terminal_size().columns
    for linha in texto.split('\n'):
        linha_centralizada = linha.center(largura_terminal)
        for c in linha_centralizada:
            print(c, end='', flush=True)
            time.sleep(0.009)
        print()
    pygame.mixer.music.stop()



if __name__ == '__main__':
    pass
