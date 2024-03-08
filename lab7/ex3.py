import pygame
pygame.init()
screen = pygame.display.set_mode((680,480))
pygame.display.set_caption("RED BALL GAME")
icon = pygame.image.load('images/ball.png')
pygame.display.set_icon(icon)
radius = 25
speed = 20
red = (255,0,0)
x = screen.get_width()/2
y = screen.get_height()/2
done = False
while not done:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y-speed,radius)
            elif event.key == pygame.K_DOWN:
                y = min(y+speed,screen.get_height()-radius)
            elif event.key == pygame.K_LEFT:
                x = max(x - speed,radius)
            elif event.key == pygame.K_RIGHT:
                x = min(x+speed,screen.get_width()- radius)
    pygame.draw.circle(screen,red,(x,y),radius)
    pygame.display.flip()
pygame.quit()