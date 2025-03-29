import pygame
from constants import *
from player import Player

def main():
    # Start Game
    pygame.init()

    # Initiate clock with arg for 60 fps freq
    clock = pygame.time.Clock()
    dt = 0
    tick_delta = clock.tick(60)
    dt = tick_delta / 1000
    
    # Initialize Screen Object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Instance of Player object
    player = Player(x= SCREEN_WIDTH /2, y= SCREEN_HEIGHT /2)
    

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0)) # Fill Screen with black
        player.draw(screen) # Draw Player
        pygame.display.flip()

    # Testing Console Outputs
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()