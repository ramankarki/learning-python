import pygame

pygame.init()

window_width = 700
window_height = 600

color = (255,0,255)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("events")
clock = pygame.time.Clock()

duke = pygame.image.load("duke.png")
duke_rect = duke.get_rect()
duke_rect.center = (window_width/2, window_height/2)

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    

    window.fill(color)
    window.blit(duke, duke_rect)
    pygame.display.flip()
    clock.tick(60)


