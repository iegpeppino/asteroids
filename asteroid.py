import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super(Asteroid, self).__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(
            surface= screen,
            color= "white",
            center= self.position,
            radius= self.radius,
            width= 2 
            )

    def update(self, dt):
       self.position += (self.velocity * dt)

    """
    This method is called when a collision between a projectile
    and the asteroid is detected.
    First it kills the current asteroid sprite, then checks its size
    if it is bigger than the smaller possible size, two smaller asteroids
    are created with opposite velocity vectors set at a random angle from 20° to 50°
    """
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(rand_angle)
            vect2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = vect1 * 1.2
            asteroid_2.velocity = vect2 * 1.2
            return asteroid_1, asteroid_2