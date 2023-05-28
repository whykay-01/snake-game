import pygame

def basics():
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Snake Game")
    return screen

def blue():
    return (0,0,255)

def main():
    pygame.init()
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
        pygame.draw.rect(basics(), blue(),[200,150,10,10])
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()