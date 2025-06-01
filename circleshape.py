import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, collider):
        return self.position.distance_to(collider.position) <= self.radius + collider.radius
        #distance = pygame.math.Vector2.distance_to(self.position, collider.position)
        #if distance <= self.radius + collider.radius:
        #    return True
        #return False

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
