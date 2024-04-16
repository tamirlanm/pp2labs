import pygame
pygame.init()
screen = pygame.display.set_mode((860,680))
icon = pygame.image.load("images/iconex3.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("RED BALL GAME")
clock = pygame.time.Clock
running = True
red = (255,0,0)
ball_x = screen.get_width()//2
ball_y = screen.get_height()//2
red_rad = 25
while running:
    screen.fill("white")
    pygame.draw.circle(screen,"red",(ball_x,ball_y),25)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if ball_y - 20 >= red_rad:
                ball_y -= 20
        if keys[pygame.K_DOWN]:
            if ball_y + 20 <= screen.get_height() - red_rad:
                ball_y += 20
        if keys[pygame.K_LEFT]:
            if ball_x - 20 >= red_rad:
                ball_x -= 20
        if keys[pygame.K_RIGHT]:
            if ball_x + 20 <= screen.get_width() - red_rad:
                ball_x += 20
