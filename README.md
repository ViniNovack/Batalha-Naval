# 🚀 Star Wars: Batalha Naval

> *"Que a Força esteja com você."*

Um jogo de **Batalha Naval temático de Star Wars** rodando inteiramente no terminal, feito em Python com narração cinematográfica, trilha sonora original, arte ASCII e dois modos de jogo completamente distintos. Cada ataque, acerto e erro é narrado no universo de uma galáxia muito, muito distante.

---

## 🗂️ Sumário

- [🎯 Visão Geral](#-visão-geral)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🎮 Modos de Jogo](#-modos-de-jogo)
- [⚙️ Sistema de Armas](#️-sistema-de-armas)
- [🗺️ O Campo de Batalha 10×10](#️-o-campo-de-batalha-10×10)
- [🔫 Sistema de Ataque](#-sistema-de-ataque)
- [💬 Diálogo Randômico por Facção](#-diálogo-randômico-por-facção)
- [🩸 Sistema de Dano Dinâmico](#-sistema-de-dano-dinâmico)
- [⌨️ Engine de Texto Typewriter](#️-engine-de-texto-typewriter)
- [🎵 Trilha Sonora Dinâmica](#-trilha-sonora-dinâmica)
- [🖼️ Sistema de ASCII Art](#️-sistema-de-ascii-art)
- [🏁 Dois Finais Cinematográficos](#-dois-finais-cinematográficos)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [▶️ Como Executar](#️-como-executar)
- [👥 Autores](#-autores)

---

## 🎯 Visão Geral

Este não é apenas um jogo de Batalha Naval — é uma **experiência cinematográfica**. Da abertura com a Marcha Principal de Star Wars até os finais dramáticos por facção, cada momento foi criado para imergir o jogador no conflito entre o **Império Galáctico** e a **Resistência**. O jogo inteiro roda no terminal usando arte ASCII, códigos de cor ANSI, música dinâmica e uma engine de texto typewriter personalizada.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00979D?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

**Bibliotecas:** `pygame` · `random` · `os` · `time` · `shutil`

> ⚠️ `os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'` é definido no topo de cada módulo para suprimir o banner de inicialização do pygame, mantendo o terminal limpo para a experiência cinematográfica.

---

## 🎮 Modos de Jogo

### ⚔️ 1. Humano vs Bot (`humano_bot.py`)
- O jogador **escolhe um lado** — Império ou Resistência
- Cada lado recebe narração de abertura, música e cutscenes em ASCII art exclusivos
- O jogador **posiciona suas armas manualmente** no grid
- O **bot posiciona suas armas aleatoriamente** usando `random.randrange()` — sem interação do jogador
- Durante o combate, o jogador ataca manualmente enquanto o **bot responde com coordenadas aleatórias**, evitando células já atacadas:

```python
# Loop de ataque do bot — resorteai até encontrar uma célula não tentada
x = random.randrange(0, 10)
y = random.randrange(0, 10)
while mAtH[y][x] != 0:
    x = random.randrange(0, 10)
    y = random.randrange(0, 10)
```

### 👥 2. Humano vs Humano (`humano_humano.py`)
- **Dois jogadores** se alternam na mesma máquina
- O Jogador 1 escolhe seu lado — Império ou Resistência — e o Jogador 2 comanda a facção oposta
- Cada jogador **posiciona secretamente** suas armas antes da batalha começar
- Os turnos se alternam com a música trocando entre **Marcha Imperial** e **Marcha da Resistência**
- A função retorna `1` para vitória do Império ou `2` para vitória da Resistência, que o `main.py` usa para rotear ao final cinematográfico correto

---

## ⚙️ Sistema de Armas

Antes da batalha, cada jogador posiciona exatamente **5 armas** que devem somar **exatamente 15 de HP** — nem mais, nem menos. A função `incluirNaves()` impõe isso com um loop `while vida != 15` e também **bloqueia combinações que ultrapassariam 15**, alertando o jogador em tempo real:

```python
def incluirNaves(m):
    vida = 0
    while vida != 15:
        # ...
        match n:
            case 1:
                if(vida == 12 or vida == 14):  # Ultrapassaria 15
                    print('❌ Sua vida ultrapasará 15, escolha outro canhão. ❌')
                else:
                    # posiciona arma, vida += 2
            case 2:
                if(vida == 14 or vida == 13 or vida == 11):  # Ultrapassaria 15
                    # bloqueia posicionamento
                # else: posiciona arma, vida += 3
            case 3:
                if(vida == 14 or vida == 13 or vida == 12 or vida == 10):  # Ultrapassaria 15
                    # bloqueia posicionamento
                # else: posiciona arma, vida += 4
    return vida
```

Existem 3 tipos de arma, cada uma usando símbolos Unicode para representar seu formato no grid:

| # | Formato Visual | Células | HP | Observação |
|---|---|---|---|---|
| 1 | `◀ ▩` | 2 horizontal | +2 HP | `◀` marca a ponta |
| 2 | `◀ ▩ ▩` | 3 horizontal | +3 HP | `◀` marca a ponta |
| 3 | `◀ ▩ ▩` + `▩` abaixo | 4 células (formato L) | +4 HP | Requer espaço na linha+1 |

A validação de coordenadas é feita por funções dedicadas que verificam **tanto o intervalo quanto o encaixe** antes de aceitar a entrada:

```python
def verif_cordenada_X(size):
    # Valida que x está em range(0,10) E que x+size também cabe no grid
    # Impede armas de serem posicionadas parcialmente fora da tela
    if x in range(0, 10):
        if x+size in range(0, 10):
            return x
```

---

## 🗺️ O Campo de Batalha 10×10

O jogo usa uma **matriz 10×10** de zeros como campo de batalha base, criada por `funcoes.matriz10()`:

```python
def matriz10():
    return [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            # ... 10 linhas no total
            ]
```

Cada modo de jogo cria **quatro matrizes por partida**:
- `mA` / `mH` — Grid de posicionamento de armas do Jogador A
- `mB` / `mR` — Grid de posicionamento de armas do Jogador B (ou Bot)
- `mAAttack` / `mAtH` — Grid de registro de ataques do Jogador A
- `mBAttack` / `mAtR` — Grid de registro de ataques do Jogador B (ou Bot)

Os grids de ataque usam dois marcadores especiais para rastrear o histórico:
- `'X'` — um **acerto** (célula continha uma peça de arma)
- `'#'` — um **erro** (célula vazia)

Ambos os grids de ataque são renderizados **lado a lado** durante o combate via `showFields()`, usando símbolos Unicode para cabeçalhos e rótulos de linha (`⊽` para colunas, `⊳` para linhas), com o HP de ambos os jogadores exibido abaixo de seus respectivos grids.

---

## 🔫 Sistema de Ataque

Cada ataque passa pela função `atacar()`, que verifica se a célula alvo contém uma peça de arma (`◀` ou `▩`):

```python
def atacar(x, y, m, mAttack):
    if(m[y][x] != 0):          # ACERTO — célula tem uma peça de arma
        pygame.mixer.music.pause()
        som_explosao = pygame.mixer.Sound("explosao.ogg")
        som_explosao.set_volume(1)
        som_explosao.play()
        time.sleep(4)           # Pausa dramática durante a explosão
        pygame.mixer.music.unpause()
        mAttack[y][x] = 'X'
        return True
    else:                       # ERRO — célula vazia
        mAttack[y][x] = '#'
        return False
```

Note como em um **acerto**, a música de fundo **pausa**, o som de explosão toca no volume máximo por 4 segundos e então a música **retoma** — uma escolha deliberada de design de áudio para tornar cada acerto impactante.

Se um jogador tentar atacar uma célula que já atacou, `jogadasAtaque()` captura isso com uma mensagem personalizada:

```python
if(mAttack[y][x] != 0):
    print('❌ Você já tentou aí! É ASSIM QUE QUER VENCER? ❌')
```

---

## 💬 Diálogo Randômico por Facção

Cada acerto e erro dispara uma **linha de diálogo selecionada aleatoriamente** específica de cada facção. `falas_do_imperio()` e `falas_da_resistencia()` contêm **3 linhas de erro** e **4 linhas de acerto** cada, escolhidas com `random.randrange()` e o `match/case` do Python:

```python
def falas_do_imperio(parametro):
    if parametro == 1:   # ERRO
        x = random.randrange(1, 4)
        match x:
            case 1: y = 'Tiro perdido. Inaceitável. O Império exige perfeição.'
            case 2: y = 'Os rebeldes são escorregadios… mas a sorte deles tem um fim.'
            case 3: y = 'Ajustem as miras! Não desperdicem munição imperial!'
    elif parametro == 2: # ACERTO
        x = random.randrange(1, 5)
        match x:
            case 1: y = 'Impacto confirmado. Mais um fragmento da nave foi destruído.'
            case 2: y = 'Os rebeldes pagam o preço de desafiar o Imperador.'
            case 3: y = 'Fogo certeiro! A galáxia logo voltará à ordem imperial.'
            case 4: y = 'O Império não tolera rebeldes!!'
```

Isso significa que **nenhuma batalha é igual** — a aleatoriedade narrativa mantém cada partida sempre diferente.

---

## 🩸 Sistema de Dano Dinâmico

A saúde da nave é dividida em **4 estágios visuais de dano**. Conforme o HP cai, a arte ASCII da nave em `funcoes.py` (`masc_imperio` / `masc_resistencia`) se degrada progressivamente — buracos aparecem no casco, partes se desprendem — controlado por um bloco `match/case`:

```python
def mostrar_nave(nave, vida, paramet):
    if vida > (paramet * 3):    x = 1   # Saúde plena
    elif vida > (paramet * 2):  x = 2   # Dano leve
    elif vida > (paramet * 1):  x = 3   # Dano pesado
    else:                       x = 4   # Dano crítico
```

`paramet` é calculado como `vida_total // 4`, dividindo o HP total em quatro bandas de limiar iguais. Cada estágio também dispara **narração de batalha única** com texto diferente para acerto e erro por facção — dando ao jogador feedback narrativo em tempo real sobre o estado da batalha.

---

## ⌨️ Engine de Texto Typewriter

Toda a narração da história é entregue por uma função typewriter personalizada que alterna entre **velocidades de impressão lenta e rápida**, com um efeito sonoro de digitação tocando em sincronia:

```python
def texto_star_wars(texto, nud=11, nur=61):
    som_digitando = pygame.mixer.Sound("digitando.ogg")
    som_digitando.play(-1)     # Loop do som de digitação
    # ...
    for c in linha_centralizada:
        if c == ' ':
            print(c, end='', flush=True)
        else:
            if x == 1:         # Modo LENTO
                print(c, end='', flush=True)
                time.sleep(0.2)
                y += 1
                if y == nud:   # Após 'nud' chars, troca para rápido
                    x = 2
            elif x == 2:       # Modo RÁPIDO
                print(c, end='', flush=True)
                time.sleep(0.02)
                y += 1
                if y == nur:   # Após 'nur' chars, volta para lento
                    x = 1
    som_digitando.stop()
```

- `nud=11` — número de caracteres impressos lentamente antes de trocar para rápido
- `nur=61` — número de caracteres impressos rapidamente antes de voltar para lento
- `flush=True` — força a saída imediata no terminal, essencial para o efeito caractere a caractere em tempo real
- Uma variante `texto_star_wars_sem_musica()` faz o mesmo mas sem o som de digitação, usada quando a música de fundo já está tocando

---

## 🎵 Trilha Sonora Dinâmica

A música muda contextualmente ao longo do jogo. Cada faixa é um arquivo de áudio `.ogg` carregado e tocado via `pygame.mixer`:

| Momento | Faixa |
|---|---|
| Menu principal e abertura | `Star-Wars-Main-Theme-_Full_.ogg` |
| Tela de seleção de facção | `Audio_-Star-Wars-Epic.ogg` |
| Turnos e cutscenes do Império | `Star-Wars-Imperial-March.ogg` |
| Turnos da Resistência | `March-of-the-Resistance.ogg` |
| Resistência em batalha | `audio_batalha_resistencia.ogg` |
| Final vitória do Império | Marcha Imperial → `respiração.ogg` (respiração de Vader) |
| Final vitória da Resistência | `22-Ben-Kenobi_s-Death-Tie-Fighter-Attack.ogg` → `Audio_-Star-Wars-Epic.ogg` |

---

## 🖼️ Sistema de ASCII Art

Todos os visuais em `funcoes_imagens.py` são renderizados usando arte ASCII em strings multilinha, centralizados dinamicamente no terminal usando `shutil.get_terminal_size()`:

```python
largura_terminal = shutil.get_terminal_size().columns
for linha in nave.split('\n'):
    linha_centralizada = linha.center(largura_terminal)
    print(linha_centralizada)
```

Isso garante que os visuais fiquem corretos independentemente da largura do terminal. Os seguintes visuais estão incluídos:

| Função | Visual |
|---|---|
| `titulo()` | Logo de Star Wars em arte ASCII |
| `episodio()` | Card de título do episódio |
| `texto()` | Texto de abertura (opening crawl) |
| `escudos_lado_a_lado()` | Escudos do Império e da Resistência lado a lado para seleção de facção |
| `masc_imperio(s)` | Destruidor Imperial em 4 estágios de dano (s=1 a 4) |
| `masc_resistencia(s)` | Nave da Resistência em 4 estágios de dano (s=1 a 4) |
| `comandante_imperial()` | Retrato do comandante imperial |
| `dentro_da_nave_resistencia()` | Interior da nave da Resistência |
| `imagem_texto_batalha()` | Card cinematográfico de início de batalha |
| `esploção_das_naves()` | Efeito de explosão para os finais |
| `imagem_nave_indo_em_bora()` | Nave da Resistência escapando para o hiperespaço |
| `imagem_fim()` | Tela final "The End" |

---

## 🏁 Dois Finais Cinematográficos

### 🔴 Vitória do Império (`final_imperio_vencedor.py`)
A nave da Resistência é destruída. A **Marcha Imperial** toca enquanto os generais comemoram — até que uma nave misteriosa atraca no hangar. *"É do Lord…"* — então a música para abruptamente. A **respiração de Darth Vader** (`respiração.ogg`) preenche o terminal por 10 segundos de silêncio antes da tela final.

### 🔵 Vitória da Resistência (`final_rebeldes_vencedores.py`)
A Resistência rompe o bloqueio. Uma faixa de **Ataque dos Caças TIE** toca enquanto o Império percebe que falhou — então muda para uma faixa **Épica de Star Wars** enquanto a tripulação comemora. A nave escapa para o hiperespaço antes da tela final.

Ambos os finais são módulos independentes que podem ser executados separadamente via `if __name__ == '__main__'`.

---

## 📁 Estrutura do Projeto

| 📄 Arquivo | 📖 Descrição |
|---|---|
| `main.py` | Ponto de entrada — abertura, menu principal, música e roteamento para o modo de jogo |
| `humano_bot.py` | Modo Humano vs Bot — loop completo de jogo com IA do bot e narração cinematográfica |
| `humano_humano.py` | Modo Humano vs Humano — turnos alternados com seleção de facção |
| `funcoes.py` | Lógica central do jogo — posicionamento de armas, sistema de ataque, diálogo, exibição de saúde, engine typewriter, renderização do grid |
| `funcoes_imagens.py` | Toda a arte ASCII — naves em 4 estágios de dano, explosões, retratos, tela de título, telas de final |
| `final_imperio_vencedor.py` | Sequência cinematográfica de final de vitória do Império |
| `final_rebeldes_vencedores.py` | Sequência cinematográfica de final de vitória da Resistência |

---

## ▶️ Como Executar

Certifique-se de ter **Python 3.10+** e **pygame** instalados:

```bash
pip install pygame
```

Em seguida execute:

```bash
python main.py
```

> ⚠️ Todos os arquivos de áudio `.ogg` devem estar no **mesmo diretório** que os scripts para a música e os efeitos sonoros funcionarem.
>
> ⚠️ **Python 3.10 ou superior** é obrigatório — o jogo usa `match/case` (correspondência estrutural de padrões) extensivamente em todo o código.

---

## 👥 Autores

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ViniNovack">
        <img src="https://github.com/ViniNovack.png" width="100px" style="border-radius: 50%;" alt="ViniNovack"/>
        <br/>
        <sub><b>Vinicius Novack</b></sub>
      </a>
      <br/>
      <a href="https://github.com/ViniNovack">
        <img src="https://img.shields.io/badge/ViniNovack-181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/carolinacassaro">
        <img src="https://github.com/carolinacassaro.png" width="100px" style="border-radius: 50%;" alt="carolinacassaro"/>
        <br/>
        <sub><b>Carolina Faria Cassaro</b></sub>
      </a>
      <br/>
      <a href="https://github.com/carolinacassaro">
        <img src="https://img.shields.io/badge/carolinacassaro-181717?style=flat-square&logo=github&logoColor=white"/>
      </a>
    </td>
  </tr>
</table>

*Feito com 💙 na PUCPR*

</div>
