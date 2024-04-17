# Импорт библиотек и настройка окна и параметров игры
import pygame
import sys
import random
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((840, 600))

pygame.display.set_caption("Game")

# Загрузка изображения дороги
road =  pygame.image.load('images/road.png')

# Установка частоты кадров
FPS = 60
FramePerSec = pygame.time.Clock()

speed = 2

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Установка шрифтов для отображения текста
font = pygame.font.SysFont("Verdana", 100)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка изображения монеты
coin = pygame.image.load('images2/coin.png')
coin.set_colorkey(WHITE)
coin = pygame.transform.scale(coin, (20, 20))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/car1.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (102, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    # Обновление положения игрока
    def update(self, score):
        fail = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.x > 140:
            self.rect.x -= 3 * speed
        if keys[pygame.K_d] and self.rect.x < 605:
            self.rect.x += 3 * speed

        if pygame.sprite.spritecollide(self, cars, False):
            fail = True
        if pygame.sprite.spritecollide(self, coins, False):
            coin_in_road.rect.y = - 200
            lines = [190, 320, 440, 570]
            line = random.randint(0, 3)
            coin_in_road.rect.x = lines[line]
            score += random.randint(1, 5)
        
        return fail, score
    
    # Отрисовка игрока на экране
    def draw(self):
        window.blit(self.image, self.rect)

# Класс машины противника
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/car2.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Обновление положения машины противника
    def update(self):
        lines = [180, 300, 440, 570]
        self.rect.y += 2 * speed
        line = random.randint(0, 3)
        if self.rect.y > 800:
            self.rect.y = - 300
            self.rect.x = lines[line]
    
    # Отрисовка машины противника на экране
    def draw(self):
        window.blit(self.image, self.rect)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images2/coin.png')
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    # Обновление положения монеты
    def update(self):
        lines = [190, 320, 440, 570]
        self.rect.y += 2 * speed
        line = random.randint(0, 3)
        if self.rect.y > 700:
            self.rect.y = - 200
            self.rect.x = lines[line]
        if pygame.sprite.spritecollide(self, cars, False):
           self.rect.y = - 200
           self.rect.x = lines[line]
    
    # Отрисовка монеты на экране
    def draw(self):
        window.blit(self.image, self.rect)

# Создание экземпляра игрока
player = Player(180, 430)

# Создание групп спрайтов для машин и монет
cars = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Создание монеты на дороге
coin_in_road = Coin(190, -100)
coins.add(coin_in_road)

# Создание машин противников
for i in range(2):
    car = Car(570, 130)
    cars.add(car)
    car = Car(570, -330)
    cars.add(car)

y1 = 0
y2 = -600

fail = False

score = 0

# Главный игровой цикл
while not fail:
    # обработка картинки
    window.fill((0, 0, 0))
    window.blit(road, (0, y1))
    window.blit(road, (0, y2))

    score_txt = font_small.render(str(score), True, YELLOW)
    window.blit(score_txt, (50, 50))
    window.blit(coin, (20, 52))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#движение дороги
    y1 += speed
    y2 += speed
    if y1 >= 600:
        y1 -= 1200
    elif y2 >= 600:
        y2 -= 1200

#изменение скорости
    if score > 100:
        speed = 6
    elif score > 65:
        speed = 5
    elif score > 35:
        speed = 4
    elif score > 15:
        speed = 3

    for i in cars:
        i.update()
        i.draw()
#вызов функций
    coin_in_road.update()
    coin_in_road.draw()
    
    fail, score = player.update(score)
    player.draw()
    

    pygame.display.update()
    FramePerSec.tick(FPS)

# Обработка завершения игры
while fail:
    window.fill(RED)
    window.blit(game_over, (150, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()