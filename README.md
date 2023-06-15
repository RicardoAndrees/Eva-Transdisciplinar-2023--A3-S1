# Eva-Transdisciplinar-2023--A3-S1-

# Informe del Proyecto

## Resumen

El proyecto se centra en el desarrollo de un programa utilizando Pygame para crear un juego de salto con una pelota. El objetivo del juego es mantener la pelota en el aire evitando que toque el suelo. El jugador controla la pelota mediante la tecla de espacio para realizar saltos.

## Detalles de Implementación

El programa utiliza las siguientes funcionalidades de Pygame:

1.  Inicialización del juego y configuración de la ventana.
* Para comenzar el código definimos el ancho y el alto del background determinados como pygame_width para el ancho y pygame_height para el alto.

2.  Carga de imágenes de fondo y definición de rectángulos para colisiones.
* pintamos las imágenes que usaremos a lo largo del código tales como la pelota, el fondo del background y el trampolín y se definen sus tamaños con la función get_rect creándoles variables independientes a cada uno para diferenciarlos. 

3.  Configuración del bucle principal del juego utilizando un ciclo while.
			A lo largo del ciclo while en nuestro código, tenemos   eventos presionando teclas, detectando posicion, indicando el valor de cada boton y sus respectivas funciones, declarar nuevas variables en funcion de las diferentes operaciones. Tambien el movimiento de la pelota, dibujar el fondo, trampolin, pelota y botones en ventana y mostrar los datos obtenidos a base de los calculos y posteriormente intentar graficarlos. Todo esto todavia en proceso.
			
4.  Gestión de eventos, como cerrar la ventana.
			Dentro de los eventos encontrados en el ciclo while, tenemos el que reconozca que se presionaron teclas. Esto explica el funcionamiento tambien del punto siguiente. Existe el evento para el boton izquierdo del mouse, tambien evento al presionar la tecla Enter, el cual se usa una vez escrita la velocidad deseada para el experimento. Luego el evento para la tecla Backspace, la cual borra el ultimo caracter para una modificacion en el valor de velocidad.
			
5.  Obtención del estado del teclado para controlar la pelota.
          se define la función para los distintos botones(5), 
          *Boton 1 : Pausa el balon
          *Boton 2 : Se le asigna la velocidad al balon 
          *Boton 3 :  Aumenta la velocidad del balón en la trayectoria correspondiente
          *Boton 4 : Desacelera la velocidad del balón
          *Boton 5 : Se vuelve a posicionar el balón en la posición inicial
          
6.  Actualización del gráfico mediante la trayectoria de la balón y simulación de la gravedad.
        se aplica la formula para calcular la gravedad que seria int((0.5  *  g  * (t  **  2)) /  2) y mediante esa misma formula se crea el gráfico dentro del recuadro asignado con una linea verde creando una parábola la cual no esta completamente definida en la ecuación antes nombrada 
        
7.  Detección de colisiones con el suelo y reinicio del juego.
*parte balón en la coordenada asignada
*se limita la ordenada final donde puede llegar el balón
*se realizan impresiones de imágenes como trampolín y se inserta gráfica
*se ejecuta el bucle o while principal del programa en el reinicio del juego
8.  Dibujo de elementos en la ventana, incluyendo la pelota y el cuadro de texto interactivo.
* se crean funciones como
* pinta_grafica
* pinta_background
* pinta_trampolin 
* pinta_cuadro_de_texto
* pinta_botones
https://drive.google.com/drive/folders/1vqL16PJjxLQJ9CcsJ9HFA57b31hMrEqx?usp=sharing
