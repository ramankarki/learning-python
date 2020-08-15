import pygame, time

pygame.init()

window_width = 900
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("frame")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

ball = pygame.image.load("ball.png")
duke = pygame.image.load("duke.png")

gravity = 0.25

class QueenSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)     # Start ball at top of its column
        self.y_velocity = 0    #    with zero initial velocity

    def update(self):
        self.y_velocity += gravity       # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity 
        (target_x, target_y) = self.target_posn
        dis_to_go = target_y - new_y_pos

        if dis_to_go < 0:
            self.y_velocity = -0.65 * gravity
            new_y_pos = y + self.y_velocity

        self.posn = (x, new_y_pos)       

    def draw(self, target_surface):     
        target_surface.blit(self.image, self.posn)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return ( x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -5


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
           self.anim_frame_count = (self.anim_frame_count + 1 ) % 60
           self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0,
                       50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains  pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return ( x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5


def text_render(text, color, font_size, cord, center=False):
    '''
    renders the text in given cordinate.
    params:
        text: actual text
        color: text color
        font_size = font size
        cord: cordinate of font rect (tuple)
    '''
    font_object = pygame.font.Font(None, font_size)
    font_surface = font_object.render(text, True, color)
    font_rect = font_surface.get_rect()
    font_rect.topleft = (cord[0], cord[1])
    if center:
        font_rect.center = (cord[0], cord[1])
    window.blit(font_surface, font_rect)
    return font_rect


def draw_board(square, padding, border, board_width):
    color_black = True
    pygame.draw.rect(window, black, [padding-border, padding-border, board_width+border*2, board_width+border*2])
    for i in range(8):
        for j in range(8):
            if color_black:
                pygame.draw.rect(window, black, [j*square+padding, i*square+padding, square, square])
                color_black = False
            else:
                pygame.draw.rect(window, white, [j*square+padding, i*square+padding, square, square])
                color_black = True
        if color_black:
            color_black = False
        else:
            color_black = True


def draw_queen(board, square, padding):
    for x,y in enumerate(board):
        window.blit(ball, (x*square+padding, y*square+padding))


board_width = 680
square = 85
padding = 10
border = 2
board = [6, 4, 2, 0, 5, 7, 1, 3]

all_queen = []
for x,y in enumerate(board):
    queen = QueenSprite(ball, (x*square+padding, y*square+padding))
    all_queen.append(queen)

# Instantiate two duke instances, put them on the chessboard
duke_animation = DukeSprite(duke,(800, 350))

# Add them to the list of sprites which our game loop manages
all_queen.append(duke_animation)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = event.pos
            for queens in all_queen:
                if queens.contains_point(posn_of_click):
                    queens.handle_click()
                    break

    for queen in all_queen:
        queen.update()

    window.fill(white)
    draw_board(square, padding, border, board_width)
    # draw_queen(board, square, padding)
    for queen in all_queen:
        queen.draw(window)

    pygame.display.update()
    clock.tick(60)


