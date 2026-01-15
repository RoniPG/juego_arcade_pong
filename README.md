# :video_game: Pong Clone

Proyecto sencillo de clon de Pong escrito en Python usando el módulo `turtle`.

 ## :dart: Objetivo

- A implementar: 
  - Modo dos jugadores. :vs:
- A futuro: 
  - Modo jugador vs IA. :robot:
  - Sonidos. :musical_note: 

## :wrench: Requisitos

- Python 3.11
- Conda o Miniconda (recomendado)
- Entorno `pong_env` con las dependencias instaladas.

## :checkered_flag: Puesta en marcha

#### 1. Clona el repositorio:

```bash
git clone https://github.com/RoniPG/juego_arcade_pong.git
cd juego_arcade_pong
````

#### 2. Instalar python 3.11:

- 2.1 Con Linux:

```bash
sudo apt install python3.11
````

- 2.2 Con miconda (Opcional):

```bash
conda create -n pong_env python=3.11
conda activate pong_env
````

#### 3. Ejecutar juego

```bash
python src/main.py
````

## 🎮 Cómo se juega

El objetivo del juego es sencillo: **evitar que la pelota pase tu pala y conseguir más puntos que tu oponente**.

### 🕹️ Controles

**Pala izquierda (Jugador 1):**
- ⬆️ `W` → Mover hacia arriba
- ⬇️ `S` → Mover hacia abajo

**Pala derecha (Jugador 2):**
- ⬆️ `↑` Flecha arriba → Mover hacia arriba
- ⬇️ `↓` Flecha abajo → Mover hacia abajo

### ▶️ Menú del juego
Desde el menú principal puedes:
- ▶️ **Iniciar** la partida
- ⏸️ **Pausar** el juego en cualquier momento
- 🔄 **Reiniciar** la partida

### 🧠 Mecánicas básicas
- 🎾 La pelota rebota en las palas y en los bordes superior e inferior
- 🧱 Las palas no pueden salir de los límites de la pantalla
- 🏆 El juego continúa hasta que el jugador decide reiniciar o cerrar


## :hammer_and_wrench: Herramientas de desarrollo

- Formateo: `black`
- Linting: `ruff`
- Tipado: `mypy`

## 📂 Estructura del proyecto

```css
juego_arcade_pong/
├── src/
│   └── main.py
│   └── game.py
├── test/
├── pyproject.toml
├── README.md
└── .gitignore
```
