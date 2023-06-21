import pygame
import time as ti

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana de Pygame
pygame_width = 1002
pygame_height = 529

# Crear la ventana de Pygame
window = pygame.display.set_mode((pygame_width, pygame_height))

# Cargar la imagen de fondo
background_image = pygame.image.load("pygame_imagen_fondo.png")

# Cargar la imagen de la pelota
ball_image = pygame.image.load("pelota.png")

# Cargar la imagen del trampolín
trampolin_image = pygame.image.load("trampolin.png")



# Obtener las dimensiones de la pelota
ball_rect = ball_image.get_rect()

# Obtener las dimensiones del trampolín
trampolin_rect = trampolin_image.get_rect()

# Posición inicial de la pelota
initial_ball_x = 300
initial_ball_y = 380
ball_x = initial_ball_x
ball_y = initial_ball_y

# Posición del trampolín debajo de la posición inicial de la pelota
trampolin_x = 260
trampolin_y = 435

# Definir velocidad de la pelota
ball_speed = 0  # Inicialmente se establece en cero

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Definir dimensiones y posición de los botones
button_width = 100
button_height = 50
button_spacing = 10
button_x = 175
button_y = 100

ball_direction = "up"

# Posición del trampolín arriba de la posición final de la pelota
trampolin2_x = 260
trampolin2_y = 1

# Inicializar el reloj de Pygame
clock = pygame.time.Clock()

# Estado del juego
paused = False

# Datos del lanzamiento vertical
velocidad = 0
g = 9.8  # Aceleración gravitacional
tiAlturaMax = 0
AltMaxima = 0
tiempo_total = 0

# Cuadro de texto interactivo para ingresar la velocidad
input_rect = pygame.Rect(200, 50, 150, 30)
input_text = ""
input_active = False

# Fuente de texto
font = pygame.font.SysFont(None, 24)

# Función para verificar si se hizo clic en un botón
def is_button_clicked(button_rect, mouse_pos):
    return button_rect.collidepoint(mouse_pos)

# Función para mostrar los datos del lanzamiento vertical
def Pinta_Datos(velocidad):
    global tiAlturaMax, AltMaxima, tiempo_total
    tiAlturaMax = velocidad / g  # Tiempo hasta el punto máximo
    AltMaxima = (velocidad ** 2) / (2 * g)  # Altura máxima alcanzada
    tiempo_total = 2 * tiAlturaMax  # Tiempo total de vuelo

# Función para dibujar la gráfica del lanzamiento vertical
def Pinta_Grafica():
    graph_x = 700  # Posición X de la gráfica
    graph_y = 100  # Posición Y de la gráfica
    graph_width = 250  # Ancho de la gráfica
    graph_height = 200  # Altura de la gráfica

    # Dibujar el marco de la gráfica
    pygame.draw.rect(window, WHITE, (graph_x, graph_y, graph_width, graph_height), 2)

    # Dibujar el eje X
    pygame.draw.line(window, WHITE, (graph_x, graph_y + graph_height), (graph_x + graph_width, graph_y + graph_height), 2)

    # Dibujar el eje Y
    pygame.draw.line(window, WHITE, (graph_x, graph_y), (graph_x, graph_y + graph_height), 2)

    # Calcular las coordenadas de los puntos en la gráfica
    if tiempo_total != 0:

        t = 0
        x = graph_x
        y = graph_y + graph_height - int((0.5 * g * (t ** 2)) / 2)  # Calcular la posición Y de la pelota en el tiempo t
        points = [(x, y)]

        while t <= tiempo_total:
            x = graph_x + int((graph_width / tiempo_total) * t)
            y = graph_y + graph_height - int(ball_speed * t - 0.5 * g* (t**2))
            points.append((x, y))
            t += 0.1

        # Dibujar la curva del lanzamiento vertical
        pygame.draw.lines(window, GREEN, False, points, 2)

# Bucle principal de Pygame
running = True
t = 0
c = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del mouse
                mouse_pos = pygame.mouse.get_pos()
                for i, color in enumerate(colores):
                    button_rect = pygame.Rect(button_x, button_y + i * (button_height + button_spacing), button_width, button_height)
                    if is_button_clicked(button_rect, mouse_pos):
                        if i == 0:
                            paused = not paused
                        elif i == 4:
                            ball_x = initial_ball_x
                            ball_y = initial_ball_y
                            ball_speed = 0
                            paused = False
                            t = 0
                            ti.sleep(1)
                        elif i == 2:
                            ball_speed = 3
                        elif i == 3:
                            ball_speed = 1
                        elif i == 1:  # Nuevo botón para activar el cuadro de texto
                            input_active = True
                            input_text = ""

        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:  # Al presionar Enter, se ingresa la velocidad
                    try:
                        velocidad = float(input_text)
                        ball_speed = velocidad
                        Pinta_Datos(velocidad)  # Mostrar los datos del lanzamiento vertical
                        input_active = False  # Desactivar el cuadro de texto
                    except ValueError:
                        print("Error: ingrese un número válido.")
                elif event.key == pygame.K_BACKSPACE:  # Al presionar la tecla Retroceso, se borra el último carácter
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Movimiento de la pelota
    if not paused and velocidad != 0:
        ball_y = initial_ball_y - (velocidad * t - ((g * (t ** 2)) / 2))
        if ball_y > initial_ball_y:
            ball_x = initial_ball_x
            ball_y = initial_ball_y
            ball_speed = 0
            paused = False
            t = 1

    # Dibujar el fondo en la ventana
    window.blit(background_image, (0, 0))

    # Dibujar el trampolín en la ventana
    window.blit(trampolin_image, (trampolin_x, trampolin_y))

    # Dibujar la pelota en la ventana
    window.blit(ball_image, (ball_x, ball_y))

    # Dibujar los botones en la ventana
    colores = [RED, GREEN, BLUE, YELLOW, ORANGE]
    button_names = ["Botón 1", "Velocidad", "Botón 3", "Botón 4", "Botón 5"]
    for i, color in enumerate(colores):
        pygame.draw.rect(window, color, (button_x, button_y + i * (button_height + button_spacing), button_width, button_height))
        button_text = pygame.font.SysFont(None, 24).render(button_names[i], True, WHITE)
        text_x = button_x + (button_width - button_text.get_width()) // 2
        text_y = button_y + i * (button_height + button_spacing) + (button_height - button_text.get_height()) // 2
        window.blit(button_text, (text_x, text_y))

    # Dibujar la gráfica del lanzamiento vertical
    Pinta_Grafica()

    # Mostrar los datos del lanzamiento vertical en pantalla
    datos = [
        f"Velocidad inicial: {velocidad} m/s",
        f"Tiempo hasta altura máx: {tiAlturaMax:.2f} s",
        f"Altura máxima alcanzada: {AltMaxima:.2f} m",
        f"Tiempo total de vuelo: {tiempo_total:.2f} s"
    ]
    texto_velocidad = [
        f"Velocidad: {velocidad:.2f} m/s"
    ]
    for i, text in enumerate(datos):
        text_surface = font.render(text, True, WHITE)
        window.blit(text_surface, (700, 315 + i * 30))
    for i, text in enumerate(texto_velocidad):
        text_surface = font.render(text, True, WHITE)
        window.blit(text_surface, (712, 59))

    # Dibujar el cuadro de texto interactivo
    pygame.draw.rect(window, WHITE, input_rect, 2)
    input_surface = font.render(input_text, True, WHITE)
    window.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

    # Actualizar la ventana
    pygame.display.update()

    # Limitar la velocidad de fotogramas
    clock.tick(60)
    if c % 100000 == 0:
        t += 1
    c += 1

pygame.quit()