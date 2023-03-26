import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("RED BALL")
run = True
move = 20
bpos_x = 450
bpos_y = 300

while run:
    screen.fill("white")
    pygame.draw.circle(screen,"red",(bpos_x,bpos_y),25)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and bpos_x > 30:
        bpos_x -= move
    elif keys[pygame.K_RIGHT] and bpos_x <870:
        bpos_x += move
    elif keys[pygame.K_UP] and bpos_y > 40:
        bpos_y -= move
    elif keys[pygame.K_DOWN] and bpos_y < 560:
        bpos_y += move 

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    clock.tick(16)
    