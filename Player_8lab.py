import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((480,270))
pygame.display.set_caption("Player")
mp3 = pygame.image.load("images_lab/mp3.webp")
run = True
songs = ["sounds_lab/Tuesday.mp3","sounds_lab/Lose_yourself.mp3","sounds_lab/Smack_that.mp3"]
num = 0
pygame.mixer.music.load(songs[num])
pygame.mixer.music.play()

while run:
    screen.blit(mp3,(0,0))
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and num < 2:
        num+=1
        pygame.mixer.music.load(songs[num])
        pygame.mixer.music.play()
    elif keys[pygame.K_LEFT] and num > 0:
        num-=1
        pygame.mixer.music.load(songs[num]) 
        pygame.mixer.music.play()
    
    if keys[pygame.K_s]:
        pygame.mixer.music.pause()
    elif keys[pygame.K_p]:
        pygame.mixer.music.unpause()

    clock.tick(10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit