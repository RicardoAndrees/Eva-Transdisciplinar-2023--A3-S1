import pygame
import time as ti
import os
import numpy
import matplotlib.pyplot as plt

# Función para verificar si se hizo clic en un botón
def is_button_clicked(button_rect, mouse_pos):
    return button_rect.collidepoint(mouse_pos)

# Generar el gráfico de la posición de la pelota
def llamar_grafico():
    plt.plot(time_values, position_values)
    plt.title("Gráfico de posición de la pelota")
    plt.xlabel("Tiempo")
    plt.ylabel("Posición de la pelota (cm)")
    plt.xlim(0, 10)
    plt.ylim(930, 10)
    # Mostrar el gráfico en una ventana separada
    plt.show()

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

# Cargar la imagen del trampolín
trampolin_image_2 = pygame.image.load("trampolin_2.png")

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

# Posición del trampolín arriba de la posición final de la pelota
trampolin2_x = 260
trampolin2_y = 1

# Inicializar el reloj de Pygame
clock = pygame.time.Clock()

# Estado del juego
paused = False
ball_direction = "up"  # Dirección inicial de la pelota

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
                        elif i == 1:
                            llamar_grafico()  # Llama a la función llamar_grafico() cuando se hace clic en el botón 2
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
    window.blit(trampolin_image_2, (trampolin2_x, trampolin2_y))
    
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
    clock.tick(120)

pygame.quit()
