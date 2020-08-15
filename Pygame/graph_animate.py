import pygame, sys, time
from pygame.locals import *

# Setup pygame
pygame.init()

# Setup window 
window_width = 500
window_height = 500
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption("Animation")

# Setup direction variables
down_left = "down_left"
down_right = "down_right"
up_left = "up_left"
up_right = "up_right"

move_speed = 2

# Setup the colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Setup the boxes data structure
b1 = {"rect":pygame.Rect(300, 80, 50, 100), "color":red, "dir":up_right}
b2 = {"rect":pygame.Rect(200, 100, 20, 20), "color":green, "dir":up_left}
b3 = {"rect":pygame.Rect(100, 150, 60, 60), "color":blue, "dir":down_left}
boxes = [b1, b2, b3]

# Run the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface
    window_surface.fill(white)

    for b in boxes:
        # Move the box data structure
        if b["dir"] == down_left:
            b["rect"].left -= move_speed
            b["rect"].top += move_speed
        if b["dir"] == down_right:
            b["rect"].left += move_speed
            b["rect"].top += move_speed
        if b["dir"] == up_left:
            b["rect"].left -= move_speed
            b["rect"].top -= move_speed
        if b["dir"] == up_right:
            b["rect"].left += move_speed
            b["rect"].top -= move_speed

        # Check whether the box has moved out of the window
        if b["rect"].top < 0:
            # The box has moved past the top
            if b["dir"] == up_left:
                b["dir"] = down_left
            if b["dir"] == up_right:
                b["dir"] = down_right
        
        if b["rect"].right > window_width:
            # The box has moved past the right side.
            if b["dir"] == down_right:
                b["dir"] = down_left
            if b["dir"] == up_right:
                b["dir"] = up_left

        if b["rect"].bottom > window_height:
            # The box has moved past the bottom.
            if b["dir"] == down_right:
                b["dir"] = up_right
            if b["dir"] == down_left:
                b["dir"] = up_left

        if b["rect"].left < 0:
            # The box has moved past the left side.
            if b["dir"] == down_left:
                b["dir"] = down_right
            if b["dir"] == up_left:
                b["dir"] = up_right

        # Draw the box onto the surface
        pygame.draw.rect(window_surface, b["color"], b["rect"])

    # Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.01)