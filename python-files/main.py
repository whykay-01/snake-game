import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Snake Game")

blue=(0,0,255)
red=(255,0,0)
 
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(screen,blue,[200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()

