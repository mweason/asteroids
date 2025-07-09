# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import * 
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, bullets)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                raise SystemExit("Game over!")
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision_check(asteroid):
                    bullet.kill()
                    asteroid.split()

        for d in drawable:
            d.draw(screen)


        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)
        
        








if __name__ == "__main__":
    main()