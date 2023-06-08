import pygame
import time as ti
import os
import numpy
import matplotlib.pyplot as plt

# Función para verificar si se hizo clic en un botón
def is_button_clicked(button_rect, mouse_pos):
    return button_rect.collidepoint(mouse_pos)

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

# Posición inicial de la pelota
initial_ball_x = 300
initial_ball_y = 400
ball_x = initial_ball_x
ball_y = initial_ball_y

# Definir velocidad de la pelota
ball_speed = 1

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
button_x = 10
button_y = 100

# Posición del trampolín debajo de la posición inicial de la pelota
trampolin_x = 260
trampolin_y = 445

# Inicializar el reloj de Pygame
clock = pygame.time.Clock()

# Estado del juego
paused = False
ball_direction = "up"  # Dirección inicial de la pelota

#Datos lanzamineto vertical
velocidad= 0         # Velocidad de la pelota
t = 9.2           # Aceleracion gravedad
tiAlturaMax = 0   # Tiempo en llegar hasta la altura máxima
AltMaxima = 0     # Altura máxima alcanzada
tiempo_total = 0  # Tiempo total del lanzamiento

# Entrada texto con cuadro para ingresar velocidad
input_rect = pygame.Rect(800, 50, 150, 30)
input_text = ""
input_active = False
font = pygame.font.SysFont(None, 24)

# Funcion para mostrar los datos del lanzamiento
def Pinta_Datos(velocidad):
    global tiAlturaMax, AltMaxima, tiempo_total
    tiAlturaMax = velocidad / g            # Tiempo total hasta alt máx
    AltMaxima   = (velocidad ** 2) / (2*g) # Altura máx alcanzada
    tiempo_total= 2 * tiAlturaMax          # tiempo total de lanzamiento

# Variables para el registro de datos de la pelota
time_values = []
position_values = []

# Bucle principal de Pygame
running = True
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
                              # Llama a la función llamar_grafico() cuando se hace clic en el botón 2
                        elif i == 1:   # se activa la entrada de texto en el cuadro
                            input_active = True
                            input_text = ""
                        elif i == 4:
                            ball_x = initial_ball_x
                            ball_y = initial_ball_y
                            ball_speed = 1
                            ball_direction = "up"  # Reiniciar la dirección de la pelota
                            paused = False
                            ti.sleep(1)
                            # Restablecer los datos registrados
                            time_values = []
                            position_values = []
                        elif i == 2:
                            ball_speed = 3
                        elif i == 3:
                            ball_speed = 1

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
                ball_direction = "up"  # Detiene la pelota al llegar a la parte inferior

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

    # Mostrar datos lanzamiento vertical a la derecha
    Pinta_Datos = [
        f"Velocidad inicial: {velocidad} m/s",
        f"Tiempo hasta altura máx: {tiAlturaMax:.2f} s",
        f"Altura máxima alcanzada: {AltMaxima:.2f} m",
        f"Tiempo total de vuelo: {tiempo_total:.2f} s"
    ]    
    texto_velocidad = [f"Velocidad:"]

    for i,text in enumerate(Pinta_Datos):
        text_surface = font.render(text, True, WHITE)
        window.blit(text_surface, (700, 315 + i * 30))
    for i, text in enumerate(texto_velocidad):
        text_surface = font.render(text, True, WHITE)
        window.blit(text_surface, (712, 59))


    # Se pinta el cuadro de texto para la velocidad
    pygame.draw.rect(window, WHITE, input_rect, 2)
    input_surface = font.render(input_text, True, WHITE)
    window.blit(input_surface, (input_rect.x + 5, input_rect.y +5))    

    # Actualizar la ventana
    pygame.display.update()

    # Limitar la velocidad de fotogramas
    clock.tick(120)

pygame.quit()
