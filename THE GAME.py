import pygame
from constants import *
from game2 import button
from game2 import *
def start_screen():
    pygame.init()
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    img = pygame.image.load(BG_STARTSCREEN)
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HIGHT))
    screen.blit(img, (SCREEN_X, SCREEN_Y))
    button(screen, (POS_BOT_X, POS_BOT_Y), "START")
    button(screen, (POS_BOT_X2, POS_BOT_Y2), "EXIT")
    pygame.display.flip()
    click = True
    while click:
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