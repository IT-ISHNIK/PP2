class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED) #move_ip() - method for moving rectangles position
        if (self.rect.bottom > 600): # limit for y coordinate
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

for entity in all_sprites:
    screen.blit(entity.image, entity.rect)
    entity.move()
