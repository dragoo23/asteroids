# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
# import constants from another file
from constants import *
# import player shape
from player import Player
# import asteroids
from asteroid import Asteroid
# import asteroidfields
from asteroidfield import AsteroidField
# import shot projectiles
from shot import Shot

def main():
    # print("Starting pygame init...")
    pygame.init()
    # print("Creating screen...")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    # print("Creating player...")
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # print("Player created successfully!")
    # print("Entering game loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        # print("Drawing player...")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            if player.collision_check(asteroid) == True:
                print(f"Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    # print("detected collision of projectile with asteroid")
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000
    return 

if __name__ == "__main__":
    main()