import pygame
import random
import sys
import time
from pygame.locals import *

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Racer')


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 2
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("images2/AnimatedStreet.png")

clock = pygame.time.Clock()

screen.fill(WHITE)

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images2/Enemy.png")
    self.rect = self.image.get_rect()
    self.rect.center=(random.randint(40,WIDTH-40),0)

  def move(self):
    self.rect.move_ip(0,10)
    if (self.rect.bottom > 900):
        self.rect.top = 0
        self.rect.center = (random.randint(30, 370), 0)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("images2/Player.png")
    self.rect = self.image.get_rect()
    self.rect.center = (160, 520)

  def move(self):
    pressed_keys = pygame.key.get_pressed()
    if self.rect.left > 0 and pressed_keys[K_LEFT]:
      self.rect.move_ip(-5, 0)
    if self.rect.right < WIDTH and pressed_keys[K_RIGHT]:
      self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__()
      original_image = pygame.image.load("images2/coin.png").convert_alpha()

      self.image = pygame.transform.scale(original_image, (30, 30))
      self.rect = self.image.get_rect()
      self.rect.centerx = random.randint(40, WIDTH - 40)
      self.rect.top = 0

  def move(self):
      self.rect.move_ip(0, 10)
      if self.rect.bottom > HEIGHT:
          self.rect.top = 0
          self.rect.centerx = random.randint(30, WIDTH - 30)


player = Player()
enemy = Enemy()

enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
coins = pygame.sprite.Group()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer( ADD_COIN, 2000)
while True:
  for event in pygame.event.get():
      if event.type == INC_SPEED:
          SPEED += 2
      if event.type == ADD_COIN and random.randint(1, 5) == 1:
              coin = Coin()
              coins.add(coin)
      if event.type == QUIT:
          pygame.quit()
          sys.exit()

  if pygame.sprite.spritecollideany(player, coins):
      SCORE += 1
      for coin in pygame.sprite.spritecollide(player, coins, True):
          coin.kill()



  screen.blit(background, (0,0))

  for entity in all_sprites:
      screen.blit(entity.image, entity.rect)
      entity.move()
  for coin in coins:
    screen.blit(coin.image, coin.rect)
    coin.move()

  scores = font_small.render(str(SCORE), True, BLACK)
  screen.blit(scores, (10,10))

  if pygame.sprite.spritecollideany(player, enemies):
      pygame.mixer.Sound('images2/crash.wav').play()
      time.sleep(0.5)
      screen.fill(RED)
      screen.blit(game_over, (30,250))
      pygame.display.update()
      for entity in all_sprites:
          entity.kill()
      time.sleep(2)
      pygame.quit()
      sys.exit()

  pygame.display.update()
  clock.tick(60)
