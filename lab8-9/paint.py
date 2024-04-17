import pygame
import sys

pygame.init()

height = 600
panel_height = 100
width = 800

window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height - panel_height))
another_layer = pygame.Surface((width, height - panel_height))
panel = pygame.Surface((width, panel_height))

queue = []

def getRectangle(x1, y1, x2, y2):
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x1-x2)
        h = abs(y1-y2)
        return (x, y, w, h)

def getCircle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    return (x, y)

def getRadius(x1, y1, x2, y2):
    r = max(abs(x1-x2), abs(y1-y2))
    return r

def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0: return False
    if x > width-1 or y > height-panel_height-1: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)

pencil = pygame.image.load('images/pencil.png')
pencil = pygame.transform.scale(pencil, (75, 75))
rect = pencil.get_rect()
rect1 = rect.move(10, 10)
rect2 = rect.move(95, 10)
rect3 = rect.move(180, 10)
rect4 = rect.move(265, 10)
rect5 = rect.move(350, 10)
rect6 = rect.move(435, 10)
rect7 = rect.move(520, 10)
rect8 = rect.move(605, 10)

bucket = pygame.image.load('images/bucket.png')
bucket = pygame.transform.scale(bucket, (75, 75))

eraser = pygame.image.load('images/eraser.png')
eraser = pygame.transform.scale(eraser, (75, 75))

figures = pygame.image.load('images/figures.png')
figures = pygame.transform.scale(figures, (75, 75))

rectangle = pygame.image.load('images/rectangle.png')
rectangle = pygame.transform.scale(rectangle, (75, 95))

circle = pygame.image.load('images/circle.png')
circle = pygame.transform.scale(circle, (75, 75))

pallete = pygame.image.load('images/palette.png')
pallete = pygame.transform.scale(pallete, (75, 75))

BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)
VIOLETE = (128, 0, 128)

COLOR = BLUE

fill_color = COLOR

mouse_pressed = False

tool = 0
tools = 4

screen.fill(BLACK)

poligons = False
colors = False

while True:
    panel.fill(DARK_GRAY)
    if poligons:
        panel.blit(rectangle, (10, 10))
        panel.blit(circle, (95, 10))
        if tool == 1:
            pygame.draw.rect(panel, BLUE, rect1, 1)
        if tool == 4:
            pygame.draw.rect(panel, BLUE, rect2, 1)
    elif colors:
        pygame.draw.rect(panel, BLUE, (15, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, WHITE, (100, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, RED, (185, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, YELLOW, (270, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, GREEN, (355, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, ORANGE, (440, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, VIOLETE, (525, 15, 65, 65), border_radius=10)
        pygame.draw.rect(panel, BLACK, (610, 15, 65, 65), border_radius=10)
        if COLOR == BLUE:
            pygame.draw.rect(panel, BLUE, rect1, 1)
        elif COLOR == WHITE:
            pygame.draw.rect(panel, BLUE, rect2, 1)
        elif COLOR == RED:
            pygame.draw.rect(panel, BLUE, rect3, 1)
        elif COLOR == YELLOW:
            pygame.draw.rect(panel, BLUE, rect4, 1)
        elif COLOR == GREEN:
            pygame.draw.rect(panel, BLUE, rect5, 1)
        elif COLOR == ORANGE:
            pygame.draw.rect(panel, BLUE, rect6, 1)
        elif COLOR == VIOLETE:
            pygame.draw.rect(panel, BLUE, rect7, 1)
        elif COLOR == BLACK:
            pygame.draw.rect(panel, BLUE, rect8, 1)
    else:
        panel.blit(pencil, (10, 10))
        panel.blit(bucket, (95, 10))
        panel.blit(eraser, (180, 10))
        panel.blit(figures, (265, 10))
        panel.blit(pallete, (605, 10))
        if tool == 0:
            pygame.draw.rect(panel, BLUE, rect1, 1)
        elif tool == 2:
            pygame.draw.rect(panel, BLUE, rect2, 1)
        elif tool == 3:
            pygame.draw.rect(panel, BLUE, rect3, 1)
        else:
            pygame.draw.rect(panel, BLUE, rect4, 1)

    pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                x1 = pos[0]
                y1 = pos[1] - panel_height
                if tool == 0:
                    x2 = x1
                    y2 = y1
                elif tool == 2:
                    if pos[1] >= 100:
                        origin_color = screen.get_at((x1, y1))
                        if origin_color != COLOR:
                            queue.append((x1, y1))
                            screen.set_at((x1, y1), COLOR)

                            while len(queue):
                                cur_pos = queue[0]
                                queue.pop(0)
                                step(screen, cur_pos[0] + 1, cur_pos[1], origin_color,  COLOR)
                                step(screen, cur_pos[0] - 1, cur_pos[1], origin_color,  COLOR)
                                step(screen, cur_pos[0], cur_pos[1] + 1, origin_color,  COLOR)
                                step(screen, cur_pos[0], cur_pos[1] - 1, origin_color,  COLOR)
                if tool == 3:
                    pygame.draw.rect(screen, BLACK, (x1-25, y1-25, 50, 50), border_radius=10)
                mouse_pressed = True
                if pos[1] < 100:
                    if poligons:
                        if 10 < pos[0] and pos[0] < 90:
                            tool = 1
                        elif 95 < pos[0] and pos[0] < 175:
                            tool = 4
                    elif colors:
                        if 10 < pos[0] and pos[0] < 90:
                            COLOR = BLUE
                        elif 95 < pos[0] and pos[0] < 175:
                            COLOR = WHITE
                        elif 180 < pos[0] and pos[0] < 260:
                            COLOR = RED
                        elif 265 < pos[0] and pos[0] < 345:
                            COLOR = YELLOW
                        elif 350 < pos[0] and pos[0] < 430:
                            COLOR = GREEN
                        elif 435 < pos[0] and pos[0] < 515:
                            COLOR = ORANGE
                        elif 520 < pos[0] and pos[0] < 600:
                            COLOR = VIOLETE
                        elif 615 < pos[0] and pos[0] < 695:
                            COLOR = BLACK
                    else:
                        if 10 < pos[0] and pos[0] < 90:
                            tool = 0
                        elif 95 < pos[0] and pos[0] < 175:
                            tool = 2
                        elif 180 < pos[0] and pos[0] < 260:
                            tool = 3
                        elif 265 < pos[0] and pos[0] < 345:
                            poligons = True
                        elif 605 < pos[0] and pos[0] < 685:
                            colors = True
                else:
                    poligons = False
                    colors = False

        if e.type == pygame.MOUSEBUTTONUP:
            another_layer.blit(screen, (0, 0))
            mouse_pressed = False

        if e.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                if tool == 0:
                    x1 = x2
                    y1 = y2
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.line(screen, COLOR, (x1, y1), (x2, y2))
                elif tool == 1:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.rect(screen, COLOR, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                elif tool == 4:
                    screen.blit(another_layer, (0, 0))
                    x2 = pos[0]
                    y2 = pos[1] - panel_height
                    pygame.draw.circle(screen, COLOR,  (getCircle(x1, y1, x2, y2)), getRadius(x1, y1, x2, y2), 2)
                elif tool == 3:
                    x2 = pos[0]
                    y2 = pos[1] - 100
                    pygame.draw.rect(screen, BLACK, (x2-25, y2-25, 50, 50), border_radius=10)
        
   

    window.blit(panel, (0, 0))
    window.blit(screen, (0, 100))
    pygame.display.update()