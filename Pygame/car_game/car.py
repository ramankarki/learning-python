import pygame, random

# initialize the pygame
pygame.init()

# setup colors
black = (0,0,0)
white = (255,255,255)
green = (124, 252, 0)
blue = (0,0,255)
red = (255,0,0)

# setup window
window_width = 900
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gameloop")
clock = pygame.time.Clock()  # frame refresh per second object
fps = 60

# loading image
car_img = pygame.image.load("car.png")
car_rect = car_img.get_rect()
car_width = 56
car_height = 110

# setting high score
high_score = 0


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


def cord_contains(rect, point):
    ''' returns true if a cordinate overlaps in rectangle. '''

    if rect[0] <= point[0] and point[0] < rect[0] + rect[2]:     # check if point exists in x-axis
        if rect[1] <= point[1] and point[1] < rect[1] + rect[3]: # check if point exists in y-axis
            return True
    return False


def has_collided(rect1, rect2):
    ''' returns True is any two rectangle has collided. '''

    if rect1[2] * rect1[3] <= rect2[2] * rect2[3]:  # compare which has bigger area
        top_left = (rect1[0], rect1[1])
        top_right = (rect1[0]+rect1[2], rect1[1])             # get co-ordinates of smaller rectangle
        bottom_right = (rect1[0]+rect1[2], rect1[1]+rect1[3])
        bottom_left = (rect1[0], rect1[1]+rect1[3])
        for x,y in [top_left, top_right, bottom_left, bottom_right]:
            if cord_contains(rect2, (x,y)):     # check if any of the cordinates overlap in bigger rectangle
                return True
        return False
    else:
        top_left = (rect2[0], rect2[1])
        top_right = (rect2[0]+rect2[2], rect2[1])
        bottom_right = (rect2[0]+rect2[2], rect2[1]+rect2[3])
        bottom_left = (rect2[0], rect2[1]+rect2[3])           # same here 
        for x,y in [top_left, top_right, bottom_left, bottom_right]:
            if cord_contains(rect1, (x,y)):
                return True
        return False


def while_collided(rect1, rect2, score):
    '''
    Stops the game when car collids with falling rectangle and ask to play again. 
    rect1 and rect2 contains tuple of four value i.e. topleft cordinates, width and height
    '''

    global high_score
    if has_collided([rect1[0],rect1[1],rect1[2],rect1[3]], [rect2[0],rect2[1],rect2[2],rect2[3]]):
        if score > high_score:    # if collids then change the high score
            high_score = score
        play_again_rect = text_render("Play again ", white, 50,(window_width/2, (window_height/2)-50), True)
        main_menu_rect = text_render("Main menu", white, 50, (window_width/2, (window_height/2)+20), True)
        pygame.display.update()
        while True:         # wait until 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                
                # mouse event if MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    if cord_contains(play_again_rect, (event.pos[0], event.pos[1])):
                        game_loop()
                    if cord_contains(main_menu_rect, (event.pos[0], event.pos[1])):
                        main_menu()


def game_start_counter(car_x,car_y,score):
    for i in range(3,0,-1):
        counter = 0
        while counter < 60:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # changing car cordinate
            car_rect.center = (car_x,car_y)

            # refreshing the window
            window.fill(green)

            # score board
            text_render(f"Score: {score}", white, 40, (10,10))
            text_render(f"High score: {high_score}", white, 40, (10,45))
            text_render(f"{i}", black, 200, ((window_width/2)-50, (window_height/2)-100))

            # bliting and updating window (showing window)
            window.blit(car_img, car_rect)
            pygame.display.update()
            clock.tick(fps)
            counter += 1


def pause():
    resume_rect = text_render("Resume", white, 50, (window_width/2,(window_height/2)-50), center=True)
    main_menu_rect = text_render("Main menu", white, 50, ((window_width/2), (window_height/2)+20), center=True)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return
            
            # mouse event if MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                if cord_contains(resume_rect, (event.pos[0], event.pos[1])):
                    return
                if cord_contains(main_menu_rect, (event.pos[0], event.pos[1])):
                    main_menu()
        clock.tick(fps)


def main_menu():
    window.fill(green)
    play_rect = text_render("Play", black, 50, (window_width/2,(window_height/2)-50), center=True)
    exit_rect = text_render("Exit", black, 50, ((window_width/2), (window_height/2)+20), center=True)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    game_loop()
            
            # mouse event if MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                if cord_contains(play_rect, (event.pos[0], event.pos[1])):
                    game_loop()
                if cord_contains(exit_rect, (event.pos[0], event.pos[1])):
                    pygame.quit()
                    exit()
        clock.tick(fps)


def game_loop():
    score = 0
    move_up = False
    move_down = False
    move_right = False
    move_left = False
    move_speed = 5
    car_speed = 5
    car_x = window_width/2
    car_y = window_height - car_height/2
    frame_counter = 1

    # trash setup
    trash1_x = random.randint(0, window_width-100)
    trash1_y = -100
    trash1_rect = pygame.Rect(trash1_x,trash1_y,100,100)
    # trash1_surface = pygame.Surface((100,100))

    trash2_x = 0
    trash2_y = -100
    trash2_rect = pygame.Rect(trash2_x,trash2_y,100,100)
    # trash2_surface = pygame.Surface((100,100))
    move_second = False

    # game start counter
    game_start_counter(car_x,car_y,score)

    # game loop
    while True:

        # check if car crashed
        while_collided(trash1_rect, car_rect, score)
        while_collided(trash2_rect, car_rect, score)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # event if KEYDOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
            
            # event if KEYUP
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_DOWN:
                    move_down = False
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False

        # move if event is true and add a boundary within window  
        if move_up and car_rect.top > 0:
            car_y -= move_speed
        if move_down and car_rect.bottom < window_height:
            car_y += move_speed
        if move_left and car_rect.left > 0:
            car_x -= move_speed
        if move_right and car_rect.right < window_width:
            car_x += move_speed

        # random cordinate for trash
        if trash1_y > window_height:
            trash1_x = random.randint(0, window_width-100)
            trash1_y = -100
            score += 1
        
        if trash2_y > window_height:
            trash2_x = random.randint(0, window_width-100)
            trash2_y = -100
            score += 1

        if trash1_y == window_height/2:
            move_second = True

        # updating values
        car_rect.center = (car_x,car_y)
        trash1_y += car_speed
        trash1_rect = pygame.Rect(trash1_x,trash1_y,100,100)

        if move_second:
            trash2_y += car_speed
            trash2_rect = pygame.Rect(trash2_x,trash2_y,100,100)

        if frame_counter == 300:
            car_speed += 1
            frame_counter = 1

        frame_counter += 1

        # refreshing the window
        window.fill(green)

        # bliting and updating window (showing window)
        pygame.draw.rect(window, red, [trash1_x, trash1_y, 100, 100])
        pygame.draw.rect(window, red, [trash2_x, trash2_y, 100, 100])
        window.blit(car_img, car_rect)

        # score board
        text_render(f"Score: {score}", white, 40, (10,10))
        text_render(f"High score: {high_score}", white, 40, (10,45))

        pygame.display.update()
        clock.tick(fps)




main_menu()