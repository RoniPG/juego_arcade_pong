"""Lógica principal del juego Pong Clone usando turtle.

De momento solo crea la ventana, las palas y el bucle principal.
Más adelante añadiremos:
- Pelota con movimiento.
- Sistema de puntuación.
- Controles de teclado.
"""

import turtle


# Constantes de configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong Clone"


# Creamos la ventana del juego
def setup_screen():
    """Configura la ventana principal del juego y la devuelve."""
    screen = turtle.Screen()
    screen.title(WINDOW_TITLE)
    screen.bgcolor("black")
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    # Desactivamos la actualización automática para tener más control.
    # Luego usaremos screen.update() en el bucle del juego.
    screen.tracer(0)

    return screen


# Creamos el bucle principal del juego
def run_game() -> None:
    """Función principal del juego.

    Aquí creamos la pantalla y ejecutamos el bucle principal.
    Más adelante iremos añadiendo:
    - Creación de palas y pelota.
    - Manejo de entradas del teclado.
    - Actualización de posiciones y detección de colisiones.
    """

    # Inicializamos la pantalla
    screen = setup_screen()

    # Inicializamos las palas
    left_paddle = create_paddel(x_position=-350)
    right_paddle = create_paddel(x_position=350)

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


# Creación de palas
def create_paddel(x_position: int) -> turtle.Turtle:
    """Crea una pala en la posición x indicada, centrada en y=0."""
    paddle = turtle.Turtle()
    paddle.speed(0)  # velocidad de animación (0 = lo más rápido)
    paddle.shape("square")
    paddle.color("white")
    # Por defecto, la forma "square" es 20x20 píxeles.
    # stretch_wid = alto, stretch_len = ancho (en múltiplos de 20).
    paddle.shapesize(stretch_wid=5, stretch_len=1)  # pala vertical, más alta que ancha

    paddle.penup()  # que no dibuje líneas al moverse
    paddle.goto(x_position, 0)  # colocamos la pala

    return paddle
