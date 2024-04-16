import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((420,200))
pygame.display.set_caption('MUSIC CONTROLLER')
icon = pygame.image.load('images/wave-sound.png')
pygame.display.set_icon(icon)
_songs = ["C:\\Users\\TamirlanM\\Desktop\\music\\Chase_Atlantic-Friends.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\ElGrandeToto (ft Ckay) - ElGrandeToto - Love Nwantiti (ft Ckay).mp3","C:\\Users\\TamirlanM\\Desktop\\music\\Billie Eilish - NDA.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\Playboi Carti feat. Bryson Tiller - Fell In Luv.mp3","C:\\Users\\TamirlanM\\Desktop\\music\\Blackbear - Idfc.mp3"]
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
play_button = pygame.Rect(40,50,60,30)
stop_button = pygame.Rect(110,50,60,30)
pause_button = pygame.Rect(180,50,60,30)
next_button = pygame.Rect(250,50,60,30)
while not done:
    screen.fill('purple')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_button.collidepoint(mouse_pos):
                play_song()
            elif stop_button.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
            elif pause_button.collidepoint(mouse_pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif next_button.collidepoint(mouse_pos):
                play_next_song()
    pygame.draw.rect(screen, 'black', stop_button)
    pygame.draw.rect(screen, 'white', play_button)
    pygame.draw.rect(screen, 'pink', pause_button)
    pygame.draw.rect(screen, 'blue', next_button)
    #screen.blit()
    pygame.display.flip()
