import random
import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            offAngle = random.uniform(20, 50)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroidOne = Asteroid(self.position.x, self.position.y, newRadius)
            asteroidTwo = Asteroid(self.position.x, self.position.y, newRadius)
            asteroidOne.velocity = self.velocity.rotate(offAngle) * 1.2
            asteroidTwo.velocity = self.velocity.rotate(-offAngle) * 1.2
