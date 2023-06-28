import pygame
import time as ti
import random
# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana de Pygame
W,D = (1001, 599)

# Crear la ventana de Pygame
window = pygame.display.set_mode((W,D))

# Cargar la imagen de fondo
background_image = pygame.image.load("pygame_imagen_fondo.png")

# Cargar la imagen de la pelota
ball_image = pygame.image.load("balon1.png")

# Cargar la imagen del trampolín
trampolin_image = pygame.image.load("trampolin.png")



# Obtener las dimensiones de la pelota
ball_rect = ball_image.get_rect()

# Obtener las dimensiones del trampolín
trampolin_rect = trampolin_image.get_rect()
H = 0

# música de fondo

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

# control volumen 

sonido_arriba = pygame.image.load('volume_up.png')
sonido_abajo = pygame.image.load('volume_down.png')
sonido_mute = pygame.image.load('volume_muted.png')
sonido_max = pygame.image.load('volume_max.png')
#lista de los puntos aleatorios en el mapa
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
trampolin_x = 260
trampolin_y = 465

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
button_x = 175
button_y = 100

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
input_rect = pygame.Rect(200, 50, 150, 30)
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
    graph_x = 700  # Posición X de la gráfica
    graph_y = 100  # Posición Y de la gráfica
    graph_width = 250  # Ancho de la gráfica
    graph_height = 200  # Altura de la gráfica

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

        # Dibujar la curva del lanzamiento vertical
        pygame.draw.lines(window, WHITE, False, points, 5)

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
        t+=0.1  ########### Agregue que se actualizara el t en cada ciclo, la pelota no se movia debido 
        if ball_y > initial_ball_y:
            ball_x = initial_ball_x
            ball_y = initial_ball_y
            ball_speed = 0
            paused = False
            t = 0 #Reinicia t a 0
            velocidad = 0 # La velocidad la vuelve a cero
    # Dibujar el fondo en la ventana para hacer el scrouling
    h_relativa = H % window.get_rect().width
    window.blit(background_image, (h_relativa - window.get_rect().width, 0))
    if h_relativa < W:
        window.blit(background_image,(h_relativa, 0))
    H -= 1

# Dibujar el trampolín en la ventana
    window.blit(trampolin_image, (trampolin_x, trampolin_y))

 # Dibujar la pelota en la ventana
    window.blit(ball_image, (ball_x, ball_y))

# Dibujar los botones en la ventana
    colores = [RED, ORANGE, BLUE, GREEN, BLACK]
    button_names = ["Botón 1", "Velocidad", "Botón 3", "Botón 4", "Botón 5"]
    for i, color in enumerate(colores):
        pygame.draw.rect(window, color, (button_x, button_y + i * (button_height + button_spacing), button_width, button_height))
        button_text = pygame.font.SysFont(None, 27).render(button_names[i], True, WHITE)
        text_x = button_x + (button_width - button_text.get_width()) // 2
        text_y = button_y + i * (button_height + button_spacing) + (button_height - button_text.get_height()) // 2
        window.blit(button_text, (text_x, text_y))



# Control del audio
    keys = pygame.key.get_pressed()

# Bajar volumen

    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        window.blit(sonido_abajo, (550, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        window.blit(sonido_mute, (550, 25))

# Subir volumen

    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        window.blit(sonido_arriba, (550, 25))
    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
        window.blit(sonido_max, (850, 25))

# Desactivar sonido

    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        window.blit(sonido_mute, (550, 25))

# Reactivar sonido

    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        window.blit(sonido_max, (550, 25))


    
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

#pinta puntos de manera aleatoria en el programa en forma de cascada
    for coord in coordenadas_list:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(window, BLACK, (x, y), 2)
        coord[1] += random.randint(1, 5)  # Mover hacia abajo de forma aleatoria

        # Reaparecer los puntos en la parte superior cuando llegan al fondo
        if coord[1] > 599:
            coord[1] = random.randint(-599, -1)
            coord[0] = random.randint(0, 999)

#posiciones del mouse

    mouse_pos = pygame.mouse.get_pos()
    x1 = mouse_pos[0]
    y1 = mouse_pos[1]

#diseño del mause

    pygame.draw.rect(window, WHITE, (x1, y1, 10, 10))

#define si el raton es visible o no

    pygame.mouse.set_visible(0)

# Actualizar la ventana

    pygame.display.update()

# Limitar la velocidad de fotogramas
    clock.tick(120)


pygame.quit()