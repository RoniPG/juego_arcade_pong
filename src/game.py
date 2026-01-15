"""Lógica principal del juego Pong Clone usando turtle.

De momento:
 - Creamos la ventana
 - Creamos las palas 
 - Controles de teclado.
 - Creamos el bucle principal.
Más adelante añadiremos:
- Pelota con movimiento.
- Sistema de puntuación.
"""

from tkinter import TclError
import turtle


# Constantes de configuración de la ventana
## Tamaño de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong Clone"

## Tamaño de la pala (en "múltiplos" de 20 px que usa turtle)
PADDLE_STRETCH_WID = 5  # alto
PADDLE_STRETCH_LEN = 1  # ancho

## La forma "square" de turtle mide 20x20 píxeles.
PADDLE_HEIGHT = 20 * PADDLE_STRETCH_WID
PADDLE_MOVE_DISTANCE = 20  # píxeles que se mueve la pala por pulsación

## Límites verticales para que las palas no se salgan de la pantalla
TOP_LIMIT = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
BOTTOM_LIMIT = -TOP_LIMIT

# Tamaño y velocidad de la pelota
BALL_SIZE = 1  # tamaño base de la forma "square"
BALL_SPEED_X = 0.5
BALL_SPEED_Y = 0.5

BALL_TOP_LIMIT = (WINDOW_HEIGHT / 2) - (BALL_SIZE / 2)
BALL_BOTTOM_LIMIT = -BALL_TOP_LIMIT



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
    Añadido:
    - Creación y movimiento de palas.
    - Manejo de entradas del teclado.
    Más adelante iremos añadiendo:
    - Creación y movimiento de la pelota.
    - Actualización de posiciones y detección de colisiones.
    """

    # Inicializamos la pantalla
    screen = setup_screen()

    # Inicializamos las palas
    ## Pala izquierda a la izquierda de la pantalla (x negativa)
    left_paddle = create_paddel(x_position=-350)
    ## Pala derecha a la derecha de la pantalla (x positiva)
    right_paddle = create_paddel(x_position=350)

    # Inicializamos la pelota
    ball = create_ball()

    #Velocidades iniciales de la pelota
    ball_dx = BALL_SPEED_X
    ball_dy = BALL_SPEED_Y

    # -------- Eventos de teclado --------
    # Para poder detectar teclas
    screen.listen()

    # Creamos funciones "wrapper" sin argumentos
    # porque onkeypress espera funciones sin parámetros.
    def left_paddle_up() -> None:
        move_paddle_up(left_paddle)

    def left_paddle_down() -> None:
        move_paddle_down(left_paddle)

    def right_paddle_up() -> None:
        move_paddle_up(right_paddle)

    def right_paddle_down() -> None:
        move_paddle_down(right_paddle)

    # Asignamos teclas:
    # - W / S para la pala izquierda
    screen.onkeypress(left_paddle_up, "w")
    screen.onkeypress(left_paddle_down, "s")

    # - Flechas ↑ / ↓ para la pala derecha
    screen.onkeypress(right_paddle_up, "Up")
    screen.onkeypress(right_paddle_down, "Down")

    # Bucle principal del juego
    running = True

    while running:
        try:
            # Actualizamos la pantalla manualmente
            screen.update()

            # LÓGICA DE LA PELOTA
            ## Mover la pelota según su velocidad
            ball.setx(ball.xcor() + ball_dx)
            ball.sety(ball.ycor() + ball_dy)

            ## Rebote en el borde superior
            if ball.ycor() > BALL_TOP_LIMIT:
                ball.sety(BALL_TOP_LIMIT)
                ball_dy *= -1  # invertimos la dirección vertical

            ## Rebote en el borde inferior
            if ball.ycor() < BALL_BOTTOM_LIMIT:
                ball.sety(BALL_BOTTOM_LIMIT)
                ball_dy *= -1  # invertimos la dirección vertical

            # COLISIÓN PALA DERECHA
            if 340 < ball.xcor() < 360 and abs(ball.ycor() - right_paddle.ycor()) < PADDLE_HEIGHT / 2:
                # Colocamos la pelota justo al borde de la pala y cambiamos dirección en X
                ball.setx(340)
                ball_dx *= -1

            # COLISIÓN PALA IZQUIERDA
            if -360 < ball.xcor() < -340 and abs(ball.ycor() - left_paddle.ycor()) < PADDLE_HEIGHT / 2:
                ball.setx(-340)
                ball_dx *= -1

            # TODO: aquí actualizaremos la lógica del juego:
            # - actualizar puntuación
            # - reset de la pelota
            # - etc.

            # Para no consumir 100% CPU, podemos hacer una pequeña pausa
            # (opcional, turtle a veces ya limita el frame rate).
            # turtle.time.sleep(0.01)  # si quisieras limitar aún más

            # Esperamos a que el usuario cierre la ventana (por si salimos del bucle)
            # screen.mainloop()
        except (turtle.Terminator, turtle.TurtleGraphicsError, TclError):
            # La ventana se ha cerrado, salimos del bucle
            running = False    
            break
        except Exception as e:
            print(f"Error inesperado en el bucle del juego: {e}")
            running = False
            break


# Creación de palas
def create_paddel(x_position: int) -> turtle.Turtle:
    """Crea una pala en la posición x indicada, centrada en y=0."""
    paddle = turtle.Turtle()
    paddle.speed(0)  # velocidad de animación (0 = lo más rápido)
    paddle.shape("square")
    paddle.color("white")
    # Definimos el tamaño de la pala
    paddle.shapesize(
        stretch_wid=PADDLE_STRETCH_WID, stretch_len=PADDLE_STRETCH_LEN
    )  # pala vertical, más alta que ancha

    paddle.penup()  # que no dibuje líneas al moverse
    paddle.goto(x_position, 0)  # colocamos la pala

    return paddle


# Movimientos de las palas
def move_paddle_up(paddle: turtle.Turtle) -> None:
    """Mueve una pala hacia arriba, respetando los límites de la ventana."""
    new_y = paddle.ycor() + PADDLE_MOVE_DISTANCE
    if new_y > TOP_LIMIT:
        new_y = TOP_LIMIT
    paddle.sety(new_y)

def move_paddle_down(paddle: turtle.Turtle) -> None:
    """Mueve una pala hacia abajo, respetando los límites de la ventana."""
    new_y = paddle.ycor() - PADDLE_MOVE_DISTANCE
    if new_y < BOTTOM_LIMIT:
        new_y = BOTTOM_LIMIT
    paddle.sety(new_y)


# Creamos la pelota
def create_ball() -> turtle.Turtle:
    """Crea la pelota en el centro de la pantalla."""
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)  # tamaño normal
    ball.penup()
    ball.goto(0, 0)
    return ball


