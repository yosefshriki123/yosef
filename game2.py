import pygame
from constants import *
from pygame.locals import *
import random
def rand_locsqrual():
    locationes = ((START_X_POS_SQU, SQUIRREL_MIN_Y), (START_X_POS_SQU + SPACE_X_POS_SQU* 1,SQUIRREL_MIN_Y ),
                  (START_X_POS_SQU+SPACE_X_POS_SQU*2, SQUIRREL_MIN_Y))
    randomloc = locationes[random.randint(0,2)]
    return randomloc
def rand_sqrual():
    initscreen()
    img = pygame.image.load(SQUIRREL_IMAGE)
    img = pygame.transform.scale \
        (img, (SQUIRREL_WIDTH, SQUIRREL_HEIGHT))
    ran_loc = rand_locsqrual()  # [x,y]
    screen.blit(img, (ran_loc))

    half_hole(ran_loc[0])
    return ran_loc

def half_hole(ran_loc):
    img = pygame.image.load(HALF_HOLE_IMAGE)
    img = pygame.transform.scale \
        (img, (HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT))
    screen.blit(img, (ran_loc, MIDLINE))

def clicksqual(squr_loc):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    ran_x = squr_loc[0]
    ran_y = squr_loc[1]
    if ran_x <= mouse_x <= ran_x + SQUIRREL_WIDTH and ran_y <= mouse_y <= \
            ran_y + SQUIRREL_HEIGHT:
        return True
    else:
        return False

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, True, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))
def start_screen():
    pygame.init()
    mouse = pygame.SYSTEM_CURSOR_HAND
    pygame.mouse.set_cursor(mouse)
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    img = pygame.image.load(BG_STARTSCREEN)
    img = pygame.transform.scale(img,(SCREEN_WIDTH, SCREEN_HIGHT))
    screen.blit(img, (SCREEN_X, SCREEN_Y))
    button(screen, (POS_BOT_X, POS_BOT_Y), "START")
    button(screen, (POS_BOT_X2, POS_BOT_Y2), "EXIT")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if POS_BOT_X <= mouse_x <= POS_BOT_X + WIDTH_BOT and POS_BOT_Y <= \
                    mouse_y <= \
                    POS_BOT_Y + HIGHT_BOT:
                main()
            elif POS_BOT_X2 <= mouse_x <= POS_BOT_X2 + WIDTH_BOT and \
                    POS_BOT_Y2 \
                    <= \
                    mouse_y <= \
                    POS_BOT_Y2 + HIGHT_BOT:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
start_screen()
def end_screen():
    button(screen, (POS_BOT_X, POS_BOT_Y), "PLAY AGAIN?")
    button(screen, (POS_BOT_X2, POS_BOT_Y2), "EXIT")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if POS_BOT_X <= mouse_x <= POS_BOT_X + WIDTH_BOT and POS_BOT_Y <= \
                    mouse_y <= \
                    POS_BOT_Y + HIGHT_BOT:
                main()
            elif POS_BOT_X2 <= mouse_x <= POS_BOT_X2 + WIDTH_BOT and \
                    POS_BOT_Y2 \
                    <= \
                    mouse_y <= \
                    POS_BOT_Y2 + HIGHT_BOT:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
def initscreen():
     global screen
     screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
     screen = pygame.display.set_mode(screen_size)
     # screen.fill(BACKGROUND)
     window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
     bg_img = pygame.image.load(BACKGROUND)
     bg_img = pygame.transform.scale(bg_img, (BACK_WIDTH, BACK_HIGHT))
     window.blit(bg_img, (0, 0))
     for i in range(0,3):
         img = pygame.image.load(CARROT_IMAGE)
         img = pygame.transform.scale(img,
                                      (CARROT_WIDTH, CARROT_HEIGHT))
         screen.blit(img, (START_X_POS_CAR+SPACE_X_POS_CAR*i, 0))
     for i in range(0, 3):
         img = pygame.image.load(HOLE_IMAGE)
         img = pygame.transform.scale(img,
                                      (HOLE_WIDTH, HOLE_HEIGHT))
         screen.blit(img, (START_X_POS_HOL+SPACE_X_POS_HOL*i, 300))
def main():
    pygame.init()
    global screen
    initscreen()
    squr_loc = rand_sqrual()  # current [x,y] = next pos הפונקציה קודם כל
    # מקבלת מקום התחלתח
    # background sounds
    bgsounds = pygame.mixer.Sound(BGSOUNDS)
    play_sound = True
    pygame.mixer.Sound.play(bgsounds,-1)
    gameoversounds = pygame.mixer.Sound('gameover.wav')
    winsound = pygame.mixer.Sound('win_game_over_sound.wav')
    mouse = pygame.SYSTEM_CURSOR_HAND
    # set mouse
    pygame.mouse.set_cursor(mouse)
    finish = False
    score = 0
    font = pygame.font.Font(None, 36)
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
                pygame.mixer.Sound.stop(bgsounds)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clicksqual(squr_loc):
                    #   הפונקציה עובדת עם הערך הקודם
                    # של הסנאי , בפעם הראשונה תעבוד על הערך הראשון שהוגדר
                    # הסנאי ורק אחרי הבדיקה והוספת נק היא תשנה את מקום הסנאי
                    score += 1
                    clicksqual_sound = pygame.mixer.Sound('squrl_click.wav')
                    pygame.mixer.Sound.play(clicksqual_sound)
                else:
                    score -= 1
                squr_loc = rand_sqrual()  # current [x,y] = next pos
        if score <= LOST_CONDITION:
            pygame.mixer.Sound.stop(bgsounds)
            if play_sound:
                pygame.mixer.Sound.play(gameoversounds)
                play_sound = False
            window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            bg_img = pygame.image.load(GAMEOVER_SCREEN)
            bg_img = pygame.transform.scale(bg_img, (BACK_WIDTH, BACK_HIGHT))
            window.blit(bg_img, (0, 0))
            # Render the text
            # Draw the text to the screen
            end_screen()
        elif score >= WIN_CONDITION:
            pygame.mixer.Sound.stop(bgsounds)
            if play_sound:
                pygame.mixer.Sound.play(winsound)
                play_sound = False
            # window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            # screen.fill(WHITE)
            window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            bg_img = pygame.image.load(WIN_SCREEN)
            bg_img = pygame.transform.scale(bg_img, (BACK_WIDTH, BACK_HIGHT))
            window.blit(bg_img, (0, 0))
            # Render the text
            # Draw the text to the screen
            end_screen()

            # exit1()
        text = font.render("Score: {}".format(score), True, (0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()
    pygame.quit()





