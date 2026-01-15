"""Lógica principal del juego Pong Clone usando turtle.

De momento:
 - Creamos la ventana
 - Creamos las palas
 - Controles de teclado.
 - Creamos el bucle principal.
 - Pelota con movimiento.
 - Sistema de puntuación.
TODO: Más adelante añadiremos:
- Vs AI
- Menú inicial
- Sonidos 
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
    - Creación y movimiento de la pelota.
    - Actualización de posiciones y detección de colisiones.
    - Sistema de puntuación.
    TODO: Más adelante iremos añadiendo:
    - Menú inicial
    - IA para jugar contra la máquina
    - Sonidos
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

    ## Velocidades iniciales de la pelota
    ball_dx = BALL_SPEED_X
    ball_dy = BALL_SPEED_Y

    # PUNTUACIÓN
    score_left = 0
    score_right = 0

    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.goto(0, (WINDOW_HEIGHT / 2) - 40)  # parte superior de la pantalla

    def draw_score() -> None:
        """Limpia y vuelve a dibujar el marcador."""
        score_pen.clear()
        score_space = "\t" * 12  # espacio entre las puntuaciones
        score_text = f"Jugador 1: {score_left} {score_space} Jugador 2: {score_right}"
        score_pen.write(score_text, align="center", font=("Courier", 16, "normal"))

    # Dibujamos el marcador inicial
    draw_score()

    # MENÚ
    ## Estados posibles: "stopped", "running", "paused"
    game_state = "stopped"

    menu_pen = turtle.Turtle()
    menu_pen.speed(0)
    menu_pen.color("white")
    menu_pen.penup()
    menu_pen.hideturtle()
    menu_pen.goto(0, 0)

    def draw_menu() -> None:
        """Muestra el estado actual y las instrucciones de control."""
        menu_pen.clear()
        if game_state == "stopped":
            text = "Estado: DETENIDO\nSPACE: empezar | P: pausar | R: reiniciar"
        elif game_state == "running":
            text = "Estado: JUGANDO\nP: pausar | R: reiniciar"
        else:  # paused
            text = "Estado: PAUSADO\nSPACE: reanudar | R: reiniciar"
        menu_pen.write(text, align="center", font=("Courier", 14, "normal"))

    draw_menu()

    # Eventos de teclado
    ## Para poder detectar teclas
    screen.listen()

    ## Creamos funciones "wrapper" sin argumentos
    # porque onkeypress espera funciones sin parámetros.
    def left_paddle_up() -> None:
        move_paddle_up(left_paddle)

    def left_paddle_down() -> None:
        move_paddle_down(left_paddle)

    def right_paddle_up() -> None:
        move_paddle_up(right_paddle)

    def right_paddle_down() -> None:
        move_paddle_down(right_paddle)

    ## Asignamos teclas:
    ## - W / S para la pala izquierda
    screen.onkeypress(left_paddle_up, "w")
    screen.onkeypress(left_paddle_down, "s")

    ## - Flechas ↑ / ↓ para la pala derecha
    screen.onkeypress(right_paddle_up, "Up")
    screen.onkeypress(right_paddle_down, "Down")

    # Controles del menú (start/pause/reboot)
    def start_game() -> None:
        nonlocal game_state
        if game_state in ("stopped", "paused"):
            game_state = "running"
            draw_menu()

    def pause_game() -> None:
        nonlocal game_state
        if game_state == "running":
            game_state = "paused"
            draw_menu()

    def reboot_game() -> None:
        nonlocal game_state, score_left, score_right, ball_dx, ball_dy
        # Reiniciar puntuación
        score_left = 0
        score_right = 0
        draw_score()

        # Reiniciar posiciones
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        ball.goto(0, 0)

        # Velocidades base
        ball_dx = BALL_SPEED_X
        ball_dy = BALL_SPEED_Y

        # Volvemos a estado detenido
        game_state = "stopped"
        draw_menu()

    # Asignamos teclas del menú
    screen.onkeypress(start_game, "space")
    screen.onkeypress(pause_game, "p")
    screen.onkeypress(reboot_game, "r")

    # Bucle principal del juego
    running = True

    while running:
        try:
            # Actualizamos la pantalla manualmente
            screen.update()

            # Solo actualizamos la lógica del juego si está "running"
            if game_state == "running":
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
                if (
                    340 < ball.xcor() < 360
                    and abs(ball.ycor() - right_paddle.ycor()) < PADDLE_HEIGHT / 2
                ):
                    # Colocamos la pelota justo al borde de la pala y cambiamos dirección en X
                    ball.setx(340)
                    ball_dx *= -1

                # COLISIÓN PALA IZQUIERDA
                if (
                    -360 < ball.xcor() < -340
                    and abs(ball.ycor() - left_paddle.ycor()) < PADDLE_HEIGHT / 2
                ):
                    ball.setx(-340)
                    ball_dx *= -1

                # GESTIÓN DE PUNTUACIÓN 
                ## Si la pelota se va muy a la derecha: punto para el jugador izquierdo
                if ball.xcor() > (WINDOW_WIDTH / 2):
                    # Punto para jugador 1
                    score_left += 1
                    draw_score()

                    # Reset de la pelota al centro, dirección hacia la izquierda
                    ball.goto(0, 0)
                    ball_dx = -abs(ball_dx)
                    ball_dy = BALL_SPEED_Y  # restablecemos velocidad vertical base

                ## Si la pelota se va muy a la izquierda: punto para el jugador derecho
                if ball.xcor() < -(WINDOW_WIDTH / 2):
                    # Punto para jugador 2
                    score_right += 1
                    draw_score()

                    # Reset de la pelota al centro, dirección hacia la derecha
                    ball.goto(0, 0)
                    ball_dx = abs(ball_dx)
                    ball_dy = BALL_SPEED_Y

            # Esperamos a que el usuario cierre la ventana
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
