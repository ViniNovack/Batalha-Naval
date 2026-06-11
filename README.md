# 🚀 Star Wars: Batalha Naval

> *"May the Force be with you."*

A **Star Wars-themed Battleship game** running entirely in the terminal, built in Python with cinematic narration, original soundtrack, ASCII art visuals, coordinate-based combat, and two fully distinct game modes. Every attack, hit, and miss is narrated in the universe of the Galaxy Far, Far Away.

---

## 🎯 Overview

This is not just a Battleship game — it's a **cinematic experience**. From the opening crawl with the Star Wars Main Theme to the dramatic faction-specific endings, every moment is crafted to immerse the player in the conflict between the **Galactic Empire** and the **Resistance**. The entire game runs in the terminal using ASCII art, ANSI color codes, dynamic music, and a custom typewriter text engine.

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00979D?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

**Libraries:** `pygame` · `random` · `os` · `time` · `shutil`

> ⚠️ `os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'` is set at the top of every module to suppress pygame's startup banner, keeping the terminal clean for the cinematic experience.

---

## 🎮 Game Modes

### ⚔️ 1. Human vs Bot (`humano_bot.py`)
- The player **chooses a side** — Empire or Resistance
- Each side gets unique opening narration, music and ASCII art cutscenes
- The player **manually places** their weapons on the grid
- The **bot places its weapons randomly** using `random.randrange()` — no player interaction needed
- During combat, the player attacks manually while the **bot fires back at random coordinates**, avoiding cells it already targeted:

```python
# Bot attack loop — keeps re-rolling until it finds an untried cell
x = random.randrange(0, 10)
y = random.randrange(0, 10)
while mAtH[y][x] != 0:
    x = random.randrange(0, 10)
    y = random.randrange(0, 10)
```

### 👥 2. Human vs Human (`humano_humano.py`)
- **Two players** take turns on the same machine
- Player 1 chooses their side — Empire or Resistance — and the other player commands the opposing faction
- Each player **secretly places** their weapons before the battle begins
- Turns alternate with faction-specific music swapping between **Imperial March** and **March of the Resistance**
- The function returns `1` for Empire victory or `2` for Resistance victory, which `main.py` uses to route to the correct ending cinematic

---

## ⚙️ Weapons System

Before the battle, each player places exactly **5 weapons** that must sum to **exactly 15 HP** — no more, no less. The `incluirNaves()` function enforces this with a `while vida != 15` loop and also **blocks combinations that would exceed 15**, alerting the player in real time:

```python
def incluirNaves(m):
    vida = 0
    while vida != 15:
        # ...
        match n:
            case 1:
                if(vida == 12 or vida == 14):  # Would exceed 15
                    print('❌ Sua vida ultrapasará 15, escolha outro canhão. ❌')
                else:
                    # place weapon, vida += 2
            case 2:
                if(vida == 14 or vida == 13 or vida == 11):  # Would exceed 15
                    # block placement
                # else: place weapon, vida += 3
            case 3:
                if(vida == 14 or vida == 13 or vida == 12 or vida == 10):  # Would exceed 15
                    # block placement
                # else: place weapon, vida += 4
    return vida
```

There are 3 weapon types, each using Unicode symbols to represent their shape on the grid:

| # | Visual Shape | Cells | Health | Placement note |
|---|---|---|---|---|
| 1 | `◀ ▩` | 2 horizontal | +2 HP | `◀` marks the tip |
| 2 | `◀ ▩ ▩` | 3 horizontal | +3 HP | `◀` marks the tip |
| 3 | `◀ ▩ ▩` + `▩` below | 4 cells (L-shape) | +4 HP | Requires row+1 space |

Coordinate validation is done by dedicated functions that check **both range and fit** before accepting input:

```python
def verif_cordenada_X(size):
    # Validates that x is in range(0,10) AND that x+size also fits in the grid
    # Prevents weapons from being placed partially off-screen
    if x in range(0, 10):
        if x+size in range(0, 10):
            return x
```

---

## 🗺️ The 10×10 Battlefield

The game uses a **10×10 matrix** of zeroes as the base battlefield, created by `funcoes.matriz10()`:

```python
def matriz10():
    return [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            # ... 10 rows total
            ]
```

Each game mode creates **four matrices per match**:
- `mA` / `mH` — Player A's weapon placement grid
- `mB` / `mR` — Player B's (or Bot's) weapon placement grid
- `mAAttack` / `mAtH` — Player A's attack record grid
- `mBAttack` / `mAtR` — Player B's (or Bot's) attack record grid

The attack grids use two special markers to track history:
- `'X'` — a **hit** (cell contained a weapon)
- `'#'` — a **miss** (empty cell)

Both attack grids are rendered **side by side** during combat via `showFields()`, using Unicode symbols for headers and row labels (`⊽` for columns, `⊳` for rows), with both players' HP displayed below their respective grids.

---

## 🔫 Attack System

Every attack goes through the `atacar()` function, which checks if the target cell contains a weapon piece (`◀` or `▩`):

```python
def atacar(x, y, m, mAttack):
    if(m[y][x] != 0):          # HIT — cell has a weapon piece
        pygame.mixer.music.pause()
        som_explosao = pygame.mixer.Sound("explosao.ogg")
        som_explosao.set_volume(1)
        som_explosao.play()
        time.sleep(4)           # Dramatic pause during explosion
        pygame.mixer.music.unpause()
        mAttack[y][x] = 'X'
        return True
    else:                       # MISS — empty cell
        mAttack[y][x] = '#'
        return False
```

Note how on a **hit**, the background music **pauses**, the explosion sound plays at full volume for 4 seconds, then the music **resumes** — a deliberate audio design choice to make each hit feel impactful.

If a player tries to target a cell they already attacked, `jogadasAtaque()` catches it with a custom message:

```python
if(mAttack[y][x] != 0):
    print('❌ Você já tentou aí! É ASSIM QUE QUER VENCER? ❌')
```

---

## 💬 Randomized Faction Dialogue

Every hit and miss triggers a **randomly selected line** of faction-specific dialogue. `falas_do_imperio()` and `falas_da_resistencia()` each hold **3 miss lines** and **4 hit lines**, picked with `random.randrange()` and Python's `match/case`:

```python
def falas_do_imperio(parametro):
    if parametro == 1:   # MISS
        x = random.randrange(1, 4)
        match x:
            case 1: y = 'Tiro perdido. Inaceitável. O Império exige perfeição.'
            case 2: y = 'Os rebeldes são escorregadios… mas a sorte deles tem um fim.'
            case 3: y = 'Ajustem as miras! Não desperdicem munição imperial!'
    elif parametro == 2: # HIT
        x = random.randrange(1, 5)
        match x:
            case 1: y = 'Impacto confirmado. Mais um fragmento da nave foi destruído.'
            case 2: y = 'Os rebeldes pagam o preço de desafiar o Imperador.'
            case 3: y = 'Fogo certeiro! A galáxia logo voltará à ordem imperial.'
            case 4: y = 'O Império não tolera rebeldes!!'
```

This means **no two battles feel the same** — the narrative randomness keeps every match fresh.

---

## 🩸 Dynamic Damage System

Ship health is divided into **4 visual damage stages**. As HP drops, the ship's ASCII art in `funcoes.py` (`masc_imperio` / `masc_resistencia`) progressively degrades — holes appear in the hull, parts break off — driven by a `match/case` block:

```python
def mostrar_nave(nave, vida, paramet):
    if vida > (paramet * 3):    x = 1   # Full health
    elif vida > (paramet * 2):  x = 2   # Light damage
    elif vida > (paramet * 1):  x = 3   # Heavy damage
    else:                       x = 4   # Critical damage
```

`paramet` is calculated as `vida_total // 4`, dividing total HP into four equal threshold bands. Each stage also triggers **unique battle narration** with different text for hit and miss per faction — giving players real-time story feedback on the state of the battle.

---

## ⌨️ Typewriter Text Engine

All story narration is delivered through a custom typewriter function that alternates between **slow and fast printing speeds**, with a typing sound effect playing in sync:

```python
def texto_star_wars(texto, nud=11, nur=61):
    som_digitando = pygame.mixer.Sound("digitando.ogg")
    som_digitando.play(-1)     # Loop the typing sound
    # ...
    for c in linha_centralizada:
        if c == ' ':
            print(c, end='', flush=True)
        else:
            if x == 1:         # SLOW mode
                print(c, end='', flush=True)
                time.sleep(0.2)
                y += 1
                if y == nud:   # After 'nud' chars, switch to fast
                    x = 2
            elif x == 2:       # FAST mode
                print(c, end='', flush=True)
                time.sleep(0.02)
                y += 1
                if y == nur:   # After 'nur' chars, switch back to slow
                    x = 1
    som_digitando.stop()
```

- `nud=11` — number of characters printed slowly before switching to fast
- `nur=61` — number of characters printed fast before switching back to slow
- `flush=True` — forces immediate terminal output, essential for the real-time character-by-character effect
- A variant `texto_star_wars_sem_musica()` does the same but without the typing sound, used when background music is already playing

---

## 🎵 Dynamic Soundtrack

Music changes contextually throughout the game. Every track is a `.ogg` audio file loaded and played via `pygame.mixer`:

| Moment | Track |
|---|---|
| Main menu & opening crawl | `Star-Wars-Main-Theme-_Full_.ogg` |
| Side selection screen | `Audio_-Star-Wars-Epic.ogg` |
| Empire turns & cutscenes | `Star-Wars-Imperial-March.ogg` |
| Resistance turns | `March-of-the-Resistance.ogg` |
| Resistance in battle | `audio_batalha_resistencia.ogg` |
| Empire victory ending | Imperial March → `respiração.ogg` (Vader breathing) |
| Resistance victory ending | `22-Ben-Kenobi_s-Death-Tie-Fighter-Attack.ogg` → `Audio_-Star-Wars-Epic.ogg` |

---

## 🖼️ ASCII Art System

All visuals in `funcoes_imagens.py` are rendered using large multi-line string ASCII art, centered dynamically in the terminal using `shutil.get_terminal_size()`:

```python
largura_terminal = shutil.get_terminal_size().columns
for linha in nave.split('\n'):
    linha_centralizada = linha.center(largura_terminal)
    print(linha_centralizada)
```

This ensures the visuals look correct regardless of terminal width. The following visuals are included:

| Function | Visual |
|---|---|
| `titulo()` | Star Wars logo in ASCII art |
| `episodio()` | Episode title card |
| `texto()` | Opening crawl story text |
| `escudos_lado_a_lado()` | Empire and Resistance shields side by side for faction selection |
| `masc_imperio(s)` | Imperial Destroyer at 4 damage stages (s=1 to 4) |
| `masc_resistencia(s)` | Resistance ship at 4 damage stages (s=1 to 4) |
| `comandante_imperial()` | Imperial commander portrait |
| `dentro_da_nave_resistencia()` | Inside the Resistance ship |
| `imagem_texto_batalha()` | "Battle begins" cinematic card |
| `esploção_das_naves()` | Explosion effect for endings |
| `imagem_nave_indo_em_bora()` | Resistance ship escaping to hyperspace |
| `imagem_fim()` | Final "The End" screen |

---

## 🏁 Two Cinematic Endings

### 🔴 Empire Victory (`final_imperio_vencedor.py`)
The Resistance ship is destroyed. The **Imperial March** plays as generals celebrate — until a mysterious ship docks in the hangar. *"It belongs to Lord…"* — then the music stops abruptly. **Darth Vader's breathing** (`respiração.ogg`) fills the terminal for 10 seconds of silence before the end screen.

### 🔵 Resistance Victory (`final_rebeldes_vencedores.py`)
The Resistance breaks through the blockade. A **Tie Fighter Attack** track plays as the Empire realizes it failed — then switches to an **Epic Star Wars** track as the crew celebrates. The ship escapes to hyperspace before the end screen.

Both endings are standalone modules that can be run independently via `if __name__ == '__main__'`.

---

## 📁 Project Structure

| 📄 File | 📖 Description |
|---|---|
| `main.py` | Entry point — opening crawl, main menu, music and game mode routing |
| `humano_bot.py` | Human vs Bot game mode — full game loop with bot AI and cinematic narration |
| `humano_humano.py` | Human vs Human game mode — alternating turns with faction selection |
| `funcoes.py` | Core game logic — weapon placement, attack system, dialogue, health display, typewriter engine, grid rendering |
| `funcoes_imagens.py` | All ASCII art — ships at 4 damage stages, explosions, portraits, title screen, ending screens |
| `final_imperio_vencedor.py` | Empire victory cinematic ending sequence |
| `final_rebeldes_vencedores.py` | Resistance victory cinematic ending sequence |

---

## ▶️ How to Run

Make sure you have **Python 3.10+** and **pygame** installed:

```bash
pip install pygame
```

Then run:

```bash
python main.py
```

> ⚠️ All `.ogg` audio files must be in the **same directory** as the scripts for the music and sound effects to work.
> 
> ⚠️ Python **3.10 or higher** is required — the game uses `match/case` (structural pattern matching) extensively throughout the codebase.

---

## 👥 Authors

Made with 💙 by **ViniNovack** and **Carolina**
