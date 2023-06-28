# Informe del Proyecto
## Resumen
El proyecto se centra en el desarrollo de un programa utilizando **Pygame** para crear un juego de salto con una pelota. El objetivo del juego es mantener la pelota en el aire evitando que toque el suelo. El jugador controla la pelota mediante la tecla de espacio para realizar saltos.

## Introducción al fenómeno físico
Un cuerpo lanzado verticalmente hacia arriba se mueve con movimiento uniformemente retardado hasta que su velocidad sea igual a cero, a esto se le conoce como lanzamiento vertical hacia arriba, es la unión de dos movimientos de tipo movimiento uniformemente acelerado, (MUA), uno de subida y el otro de bajada. Un estudio más minucioso del movimiento de la caída de los cuerpos fue realizado por el gran físico Galileo Galilei, en el siglo XVII
su formula general es la siguiente **(velocidad * tiempo - ((gravedad * (tiempo ** 2)) / 2))**
**Ejercicio:** Se lanza verticalmente un sombrero con una velocidad inicial de 50 m/s ¿Cuál será la altura luego de que han transcurrido 2 segundos?Altura del sombrero luego de 2 segundos es 80.38 m
Inicialización del juego y configuración de la ventana.


## Detalles de implementación

### Librerias.
Se realiza la instalación de bibliotecas a usar utilizando el comando “**pip3 install** librería a usar” en la **“terminal”** o en el **“cmd”** de su computador.

El programa utiliza las siguientes funcionalidades de Pygame:
Para comenzar el código definimos el ancho y el alto del **“background”** determinados como **“pygame_width”** para el ancho y **“pygame_height”** para el alto.

### Carga de imágenes de fondo y definición de rectángulos para colisiones.
Pintamos las imágenes que usaremos a lo largo del código tales como la pelota, el fondo del **“background”** y el trampolín y se definen sus tamaños con la función **“get_rect”** creándoles variables independientes a cada uno para diferenciarlos.

### Configuración del bucle principal del juego utilizando un ciclo while.
A lo largo del ciclo while en nuestro código, tenemos eventos presionando teclas, detectando posición, indicando el valor de cada botón y sus respectivas funciones, declarar nuevas variables en función de las diferentes operaciones. También el movimiento de la pelota, dibujar el fondo, trampolín, pelota y botones en ventana y mostrar los datos obtenidos a base de los cálculos y posteriormente intentar graficarlos. 

### Gestión de eventos, como cerrar la ventana.
Dentro de los eventos encontrados en el ciclo while, tenemos el que reconozca que se presionaron teclas. Esto explica el funcionamiento tambien del punto siguiente. Existe el evento para el boton izquierdo del mouse, tambien evento al presionar la tecla Enter, el cual se usa una vez escrita la velocidad deseada para el experimento. Luego el evento para la tecla Backspace, la cual borra el ultimo caracter para una modificacion en el valor de velocidad.

### Gráfico
Actualización del gráfico mediante la trayectoria de la balón y simulación de la gravedad. se aplica la formula para calcular la gravedad que seria int((0.5 * g * (t ** 2)) / 2) y mediante esa misma formula se crea el gráfico dentro de la ventana asignado con una linea, creando una parábola la cual no esta completamente definida en la ecuación antes nombrada

### Detección de colisiones con el suelo y reinicio del juego.

Parte balón en la coordenada asignada, se limita la ordenada final donde puede llegar el balón, se realizan impresiones de imágenes como trampolín y se inserta gráfica. Se ejecuta el bucle o while principal del programa en el reinicio del juego.


## Guía de uso.
La guía de uso para este código es bastante sencillo, el código consta con **5 botones** que cumplen una función por cada botón.
**1.-** El botón numero 1 es de un cuadro interactivo donde el usuario puede ingresar la gravedad que desee en el programa
**2.-** El botón numero 2 es de un cuadro interactivo donde el usuario puede ingresar la velocidad del balón que desee en el programa.
**3.-** El botón numero 3 incrementa en una velocidad determinada el balón en movimiento.
**4.-** El botón numero 4 decrementa la velocidad del balón.
**5.-** El botón numero 5 reinicia todos los datos del programa.

El usuario puede ingresar **2 datos** dentro del juego que es la **gravedad** y la **velocidad** que adquiere el balón
el usuario al momento de ingresar la gravedad y la velocidad tiene que presionar la tecla **“enter”** y el programa realizará la función de mover el balón hasta una cierta posición, esta posición es 0 hasta que la velocidad del balón se acaba.
Al momento de ingresar los datos el programa grafica los datos en función de una formula y convierte esa información en una parábola dentro del grafico.
El programa consta de una función para la musica el uso de este elemento es bastante sencillo
tiene asignado 4 teclas para subir, bajar, reanudar o detener la música, para bajar el volumen de la música se utiliza el **numero “9”**, para subir el volumen de la música se utiliza el **numero “0”**, para detener la música de utiliza la letra **“m”** y para reanudar la música se utiliza la **“,/coma”.**
gravedades dependiendo del planeta, todos en m/s^2: Luna 1.6, Mercurio 2.8, Venus 8.9, **Tierra 9.8** ,Marte 3.7, Júpiter 22.9 Saturno 9.1, Urano 7.8, Neptuno 11,15.

# Conclusiones
Aqui van las conclusiones.




### Enlace videos 1ra entrega y entrega final.
https://drive.google.com/drive/folders/1vqL16PJjxLQJ9CcsJ9HFA57b31hMrEqx

