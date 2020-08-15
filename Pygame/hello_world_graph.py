import pygame, sys
from pygame.locals import *

# setup pygame
pygame.init()

# setup the colors
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# setup the window
window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("hello world")

# setup fonts
basic_font = pygame.font.SysFont(None, 48)

# setup the text
text = basic_font.render("hello world!", True, white, blue)
textRect = text.get_rect()
textRect.centerx = window_surface.get_rect().centerx
textRect.centery = window_surface.get_rect().centery

# draw the white background onto the surface
window_surface.fill(white)

# draw a green polygon on the surface
pygame.draw.polygon(window_surface, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(window_surface, blue, (60, 60), (120, 60), 4)
pygame.draw.line(window_surface, blue, (120, 60), (60, 120))
pygame.draw.line(window_surface, blue, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(window_surface, blue, (300, 50), 20, 0)

# Draw a red ellipse onto the surface.
pygame.draw.ellipse(window_surface, red, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
pygame.draw.rect(window_surface, red, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pix_array = pygame.PixelArray(window_surface)
for line in range(500):
    pix_array[line][380] = red
del pix_array

# draw the text onto the surface
window_surface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()