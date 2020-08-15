import pygame
import moves_generator

# pygame initialize
pygame.init()

# setup colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# setup window
window_width = 1000
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Eight Queen Puzzle")
clock = pygame.time.Clock()
fps = 60
queen = pygame.image.load("queen.png")
board_width = 700


# renders any text on screen
def text_render(text, color, font_size, cord, center=False):
    text_obj = pygame.font.Font(None, font_size)
    txt_surface = text_obj.render(text, True, color)
    txt_rect = txt_surface.get_rect()
    txt_rect.topleft = (cord[0], cord[1])
    window.blit(txt_surface, txt_rect)


def draw_board_part2(i, count, square, padding):
    for j in range(10, board_width-padding, square):
            if count % 2 == 0:
                pygame.draw.rect(window, black, [j, i, square, square])
            else:
                pygame.draw.rect(window, white, [j, i, square, square])
            count += 1

# draws board on screen
def draw_board_part1(square, border, padding):
    count = 1
    x = padding - border
    y = padding - border
    width = board_width - (padding*2) + (border*2)
    height = window_height - (padding*2) + (border*2)
    pygame.draw.rect(window, black, [x, y, width, height])
    for i in range(10, window_height-padding, square):
        if count == 1:
            draw_board_part2(i, count, square, padding)
            count = 0
        else:
            draw_board_part2(i, count, square, padding)
            count = 1


# locates queen and draws on board
def draw_queen(padding, square, board):
    x = 0
    p = 20
    for y in board:
        window.blit(queen, (x + padding, y*square + p))
        x += 85


def main():
    square = 85     # size of each square
    padding = 10    # padding around board
    border = 2      # border width
    board = moves_generator.main(8)  # returns 10 possible moves

    index = 0       # index of each moves in board
    while True:
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # change move if KEYUP
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and index > 0:
                    index -= 1
                if event.key == pygame.K_RIGHT and index < len(board)-1:
                    index += 1

        # refresh window
        window.fill(white)
        # horizontal line
        pygame.draw.rect(window, black, [700, 0, 3, 700])

        # render text of number of moves
        text_render("Eight Queen Puzzle", black, 40, (722, 10))
        text_render(f"Total", black, 50, (810, 150))
        text_render(f"moves", black, 50, (800, 185))
        text_render(f"{len(board)}", black, 50, (835, 230))

        if index+1 < 10:
            add = 10
        else:
            add = 0

        text_render(f"Current", black, 50, (795, 400))
        text_render(f"move", black, 50, (815, 435))
        text_render(f"{index+1}", black, 50, (835+add, 480))
        text_render("! Use left & right arrow keys to change moves.", black, 20, (707, 678))

        # drawing board and queen and flipping buffer
        draw_board_part1(square, border, padding)
        draw_queen(padding, square, board[index])
        pygame.display.update()
        clock.tick(fps)



if __name__ == "__main__":
    main()

