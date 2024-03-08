import pygame
pygame.init()
screen = pygame.display.set_mode((420,200))
pygame.display.set_caption("MUSIC CONTROLLER")
icon = pygame.image.load('images/sound.png')
pygame.display.set_icon(icon)
pygame.mixer.init()
_songs = ["C:\\Users\\TamirlanM\\Desktop\\music\\Chase_Atlantic-Friends.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\13. Regular (English Ver.).mp3","C:\\Users\\TamirlanM\\Desktop\\music\\Billie Eilish - NDA.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\Playboi Carti feat. Bryson Tiller - Fell In Luv.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\BlackMayo - Jus  Know.mp3"]
def play_song():
    global _songs
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
done = False
play_button_rect = pygame.Rect(10,30,60,30)
stop_button_rect = pygame.Rect(90,30,60,30)
pause_button_rect = pygame.Rect(170,30,60,30)
next_button_rect = pygame.Rect(250,30,60,30)
while not done:
    screen.fill("purple")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_button_rect.collidepoint(mouse_pos):
                play_song()
            elif stop_button_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
            elif pause_button_rect.collidepoint(mouse_pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif next_button_rect.collidepoint(mouse_pos):
                play_next_song()
    pygame.draw.rect(screen,'white',play_button_rect)
    pygame.draw.rect(screen,'black',stop_button_rect)
    pygame.draw.rect(screen,'pink',pause_button_rect)
    pygame.draw.rect(screen,'gray',next_button_rect)

    pygame.display.flip()
pygame.quit()