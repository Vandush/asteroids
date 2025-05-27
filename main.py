#Python game library
import pygame

#Constant Variables
from constants import *
#Player Variables
from player import *
#Asteroid Variables
from asteroid import *

#BootDev Asteroid Field
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group()
    AsteroidField = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
   
    dt = 0
    
    #pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        #pygame.Surface.fill(screen,(0,0,0))
        screen.fill("black")

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
