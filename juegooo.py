import pygame
import time as ti
import random

# Inicializar Pygame
pygame.init()

#Dimensiones de la ventana de Pygame
W,D = (1001, 599)

#Crear la ventana de Pygame
window = pygame.display.set_mode((W,D))

# Cargar la imagen de fondo
background_image = pygame.image.load("fondo.png")

# Cargar la imagen de la pelota
ball_image = pygame.image.load("pelota.png")

# Cargar la imagen del trampolín
trampolin_image = pygame.image.load("trampolin.png")

# Cargar la imagen del atomo
atomo = pygame.image.load("atomo.png")
# Obtener las dimensiones de la pelota
ball_rect = ball_image.get_rect()

# Obtener las dimensiones del trampolín
trampolin_rect = trampolin_image.get_rect()

#posicion mapa estatico
H = 0

#puntitos en el mapa
coordenadas_list = []
for i in range(60):
    x = random.randint(0, 999)
    y = random.randint(-599, -1)  # Iniciar puntos fuera de la pantalla en la parte superior
    coordenadas_list.append([x, y])
    
# Posición inicial de la pelota
initial_ball_x = 300
initial_ball_y = 380
ball_x = initial_ball_x
ball_y = initial_ball_y

# Posición del trampolín debajo de la posición inicial de la pelota
trampolin_x = 220
trampolin_y = 450

# Definir velocidad de la pelota
ball_speed = 0  # Inicialmente se establece en cero

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0,0,0)

# Definir dimensiones y posición de los botones
button_width = 100
button_height = 50
button_spacing = 10
button_x = 40
button_y = 100

#direccion del balon
ball_direction = "up"


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
input_rect = pygame.Rect(40, 50, 150, 30)
input_text = "Ingrese velocidad: "
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
    graph_x = 650  # Posición X de la gráfica
    graph_y = 100  # Posición Y de la gráfica
    graph_width = 300  # Ancho de la gráfica
    graph_height = 300  # Altura de la gráfica

    # Dibujar el marco de la gráfica
    pygame.draw.rect(window, BLACK, (graph_x, graph_y, graph_width, graph_height), 5)

    # Dibujar el eje X
    pygame.draw.line(window, BLACK, (graph_x, graph_y + graph_height), (graph_x + graph_width, graph_y + graph_height), 5)

    # Dibujar el eje Y
    pygame.draw.line(window, BLACK, (graph_x, graph_y), (graph_x, graph_y + graph_height), 5)

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

# Variables para el registro de datos de la pelota
time_values = []
position_values = []

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
                for i, color in enumerate(colors):
                    button_rect = pygame.Rect(button_x, button_y + i * (button_height + button_spacing),
                                              button_width, button_height)
                    if is_button_clicked(button_rect, mouse_pos):
                        if i == 0:
                            paused = not paused
                        elif i == 1:
                            llamar_grafico()  # Llama a la función llamar_grafico() cuando se hace clic en el botón 2
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

        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:  # se presiona enter para ingresar velocidad
                    try:
                        velocidad = float(input_text)
                        ball_speed = velocidad
                        Pinta_Datos(velocidad)
                        input_active = False      # Se desactiva la entrada en el cuadro de texto
                    except ValueError:
                        print("Ingrese un número válido, por favor.") 
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


    # Movimiento de la pelota
    if not paused:
        if ball_direction == "up":
            ball_y -= ball_speed
            if ball_y <= 0:  # Cambiar la dirección cuando la pelota alcanza la parte superior
                ball_direction = "down"
        elif ball_direction == "down":
            ball_y += ball_speed
            if ball_y >= pygame_height - ball_rect.height:  # Cambiar la dirección cuando la pelota alcanza la parte inferior
                ball_direction = "stop"  # Detiene la pelota al llegar a la parte inferior

    # Registro de datos de la pelota
    current_time = ti.time()
    time_values.append(current_time)
    position_values.append(ball_y)

    # Dibujar el fondo en la ventana
    window.blit(background_image, (0, 0))

    # Dibujar el trampolín en la ventana
    window.blit(trampolin_image, (trampolin_x, trampolin_y))
    
    # Dibujar la pelota en la ventana
    window.blit(ball_image, (ball_x, ball_y))

    # Dibujar los botones en la ventana
    colors = [RED, GREEN, BLUE, YELLOW, ORANGE]
    button_names = ["Botón 1", "Botón 2", "Botón 3", "Botón 4", "Botón 5"]
    for i, color in enumerate(colors):
        pygame.draw.rect(window, color,
                         (button_x, button_y + i * (button_height + button_spacing), button_width, button_height))
        button_text = pygame.font.SysFont(None, 24).render(button_names[i], True, WHITE)
        text_x = button_x + (button_width - button_text.get_width()) // 2
        text_y = button_y + i * (button_height + button_spacing) + (button_height - button_text.get_height()) // 2
        window.blit(button_text, (text_x, text_y))

    # Actualizar la ventana
    pygame.display.update()

    # Limitar la velocidad de fotogramas
    clock.tick(60)
    if c % 100000 == 0:
        t += 1
    c += 1

pygame.quit()