from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.speed = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)
        if not(keys[pygame.K_w] or keys[pygame.K_s]):
            if self.speed > 0: 
                self.deccelerate(dt)
            elif self.speed < 0:
                self.deccelerate(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            pass

        self.shoot_cooldown -= dt
        self.move(dt)


    def move(self, dt):
        foward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += foward * self.speed * dt


    def accelerate(self, dt):
        if (self.speed + PLAYER_ACCELERATION * dt) > PLAYER_MAX_SPEED:
            self.speed = PLAYER_MAX_SPEED
        elif (self.speed + PLAYER_ACCELERATION * dt) < -PLAYER_MAX_SPEED:
            self.speed = -PLAYER_MAX_SPEED
        else:
            self.speed += PLAYER_ACCELERATION * dt


    def deccelerate(self, dt): 
        if (abs(self.speed) - abs(2 / 3 * PLAYER_ACCELERATION * dt)) < 0:
            self.speed = 0
        else:
            self.speed -= 2 / 3 * PLAYER_ACCELERATION * dt


    def shoot(self):
        if self.shoot_cooldown <= 0.00:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN