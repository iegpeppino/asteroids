import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draws Player Sprite
    def draw(self, screen):
        pygame.draw.polygon(surface= screen, color="white", points= self.triangle(), width= 2)

    # Rotates Player Sprite
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Moves Playe Forwards
    """
    We take a unit vector pointing straight up and rotate it so its pointin
    in the direction the player is pointing.
    Then multiply by PLAYER_SPEED * dt and add the vector to the player's postion
    """
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.timer = 0.7
        projectile = Shot(self.position[0], self.position[1])
        projectile.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return projectile

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # Rotate Left with "a" key
            self.rotate(-1*dt)
        if keys[pygame.K_d]: # Rotate Right with "d" key
            self.rotate(1*dt)
        if keys[pygame.K_w]:
            self.move(dt)   # Move Player Forwards with "w" key
        if keys[pygame.K_s]:
            self.move(-1*dt) # Move Player Backwards with "s" key
        if keys[pygame.K_SPACE]:
            if self.timer > 0.3: # Checks for timer to limit projectiles
                return
            self.shoot() # Player shoots projectiles
