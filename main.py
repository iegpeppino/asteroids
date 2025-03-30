import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Start Game
    pygame.init()

    # Initiate clock with arg for 60 fps freq
    clock = pygame.time.Clock()
    dt = 0
    tick_delta = clock.tick(60)
    dt = tick_delta / 6000
    
    # Initialize Screen Object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Group Creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Create Instance of Player object
    Player.containers = (updatable, drawable) # Add player class to groups

    player = Player(x= SCREEN_WIDTH /2, y= SCREEN_HEIGHT /2)

    # Group asteroid objects
    Asteroid.containers = (asteroids, drawable, updatable)

    # Group AsteroidField object
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0)) # Fill Screen with black
        for upd in updatable:
            upd.update(dt)    # Update all objects in updatable group
        for drw in drawable:
            drw.draw(screen) # Draw all objects in drawable group
        for asteroid in asteroids:
            if asteroid.has_colided(player):
                print("Game over!")
                return
        pygame.display.flip()

    # Testing Console Outputs
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()