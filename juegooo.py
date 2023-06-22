import pygame
import sys
import random

pygame.init()

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tamaño de la pantalla
tamaño_pantalla = (1001, 599)
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(tamaño_pantalla)

cord_x = 400
cord_y = 200

# Velocidad de movimiento del cuadrado
velocidad_x = 3
velocidad_y = 3

# Cargar imagen de fondo
fondo = pygame.image.load("pygame_imagen_fondo.png")
pelota = pygame.image.load("pelota.png")
cordenadas_list = []
for i in range(60):
    x = random.randint(0, 999)
    y = random.randint(-599, -1)  # Iniciar puntos fuera de la pantalla en la parte superior
    cordenadas_list.append([x, y])

pygame.mouse.set_visible(0)
# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if (cord_x > 999 or cord_x < 0):
        velocidad_x *= -1
    if (cord_y > 499 or cord_y < 0):
        velocidad_y *= -1

    # Cordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    x1 = mouse_pos[0]
    y1 = mouse_pos[1]

    pantalla.blit(fondo, (0, 0))

    # Dibujar 60 círculos aleatorios
    for coord in cordenadas_list:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(pantalla, RED, (x, y), 2)
        coord[1] += random.randint(1, 5)  # Mover hacia abajo de forma aleatoria

        # Reaparecer los puntos en la parte superior cuando llegan al fondo
        if coord[1] > 599:
            coord[1] = random.randint(-599, -1)
            coord[0] = random.randint(0, 999)

    cord_y += velocidad_y
    cord_x += velocidad_x

    # Zona de dibujo
    pantalla.blit(pelota, (cord_x, cord_y))

    pygame.draw.rect(pantalla, RED, (x1, y1, 10, 10))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
