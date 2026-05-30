import shutil
import time


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
    centr(imperio)
