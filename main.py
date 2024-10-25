import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *
from score import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0

    score = Score()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = timer.tick(60) / 1000
        screen.fill("black")
        
        font = pygame.font.SysFont("arialblack", 30)
        score_text = font.render(f"Score: {score.get_score()}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - 120, 10))

        for member in updatable:
            member.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                print(f"High score: {score.get_high_score()} pts")
                print(f"Your score: {score.get_score()} pts")
                score.write_high_score()
                return
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split(score)
                    shot.kill()

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()        

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()