# Asteroids

## ENG
---
### Description
This Python program lets you play a simplyfied version of the classic Asteroids game.
It is made using the "pygame" library.

### Implementation and Features
- Modular program desing for the different classes used.
- Clock set up for the game to refresh sprites at 120 fps.
- Player spaceship has movements on the screen with W,A,S,D keys.
- Player can shoot projectiles with SPACE key.
- Asteroids of different sizes are spawned at random postitions with random velocity vectors.
- Asteroids will split into two smaller asteroids when they collide with player's projectiles.
- Asteroids will be destroyed if hit at their smallest possible size.
- Game Over! is printed and the program exits if the player collides with an asteroid.

### Commentary

Some improvements will be made when I have the time.

Some of the present issues to improve are:
- Sprite objects persist after exiting the visible screen.
- No title screen or title on window.
- Lack of score system.
- Asteroids are shaped like circles.
- Some adjustments to constants are necessary for better gameplay.

---
## ESP
---
### Descripción
Este programa de Python recrea una versións simplificada del clásico juego "Asteroids".
Fué creado utilizando la librería "pygame".

### Implementación y Características del Juego
- Diseño modular para las distintas clases utilizadas en el programa.
- Se configuró un clock para actualizar la pantalla a 120 fps.
- La nave del jugador puede moverse en la pantalla utilizando las teclas W,A,S,D.
- La nave del jugador puede disparar proyectiles con la BARRA ESPACIADORA.
- Asteroides de diferentes tamaños aparecen en pantalla con vectores de movimiento aleatorios.
- Los asteroides se fragmentan en otros dos mas pequeños al detectar una colisión con los projectiles del jugador.
- Los asteroides desaparecen por completo al ser golpeados por un proyectil si su tamaño es el menor permitido por una constante.
- Se imprime "Game over!" y el programa termina si se detecta una colisión entre el jugador y un asteroide.

### Comentarios

Algunas mejoras se implementaran cuando posea mas tiempo.

Algunos de los aspectos a mejorar son:
- Los sprites persisten luego de salir de la pantalla visible.
- No hay pantalla introductoria o título en la ventana del juego.
- No hay sistema de puntuación.
- Los asteroides son solo círculos.
- Algunas de las constantes utilizadas deben ser ajustadas para mejorar la experiencia.
- Estas constantes parecen ser afectadas por la velocidad de refresco de la pantalla.
