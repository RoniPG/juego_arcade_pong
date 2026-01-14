"""Lógica principal del juego Pong Clone usando turtle.

De momento solo crea la ventana y el bucle principal.
Más adelante añadiremos:
- Palas (jugador 1 y jugador 2 / IA).
- Pelota con movimiento.
- Sistema de puntuación.
- Controles de teclado.
"""

import turtle


# Constantes de configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong Clone"


def setup_screen() -> turtle.Screen:
    """Configura la ventana principal del juego y la devuelve."""
    screen = turtle.Screen()
    screen.title(WINDOW_TITLE)
    screen.bgcolor("black")
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    # Desactivamos la actualización automática para tener más control.
    # Luego usaremos screen.update() en el bucle del juego.
    screen.tracer(0)

    return screen


def run_game() -> None:
    """Función principal del juego.

    Aquí creamos la pantalla y ejecutamos el bucle principal.
    Más adelante iremos añadiendo:
    - Creación de palas y pelota.
    - Manejo de entradas del teclado.
    - Actualización de posiciones y detección de colisiones.
    """
    screen = setup_screen()

    # Bucle principal del juego
    running = True

    while running:
        # Actualizamos la pantalla manualmente
        screen.update()

        # TODO: aquí actualizaremos la lógica del juego:
        # - mover la pelota
        # - detectar colisiones
        # - actualizar puntuación
        # - etc.

        # Para no consumir 100% CPU, podemos hacer una pequeña pausa
        # (opcional, turtle a veces ya limita el frame rate).
        # turtle.time.sleep(0.01)  # si quisieras limitar aún más

    # Esperamos a que el usuario cierre la ventana (por si salimos del bucle)
    screen.mainloop()