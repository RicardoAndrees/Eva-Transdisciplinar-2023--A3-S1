import matplotlib.pyplot as plt
import numpy as np

# Parámetros del lanzamiento
velocidad_inicial = 90  # m/s
gravedad = 9.8  # m/s^2
tiempo_total = (2 * velocidad_inicial) / gravedad

# Tiempo
tiempo = np.linspace(0, tiempo_total, num=100)

# Posición vertical
posicion = velocidad_inicial * tiempo - 0.5 * gravedad * tiempo ** 2

# Crear el gráfico
plt.plot(tiempo, posicion)

# Etiquetas y título
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.title('Lanzamiento vertical hacia arriba')

# Mostrar el gráfico
plt.show()
