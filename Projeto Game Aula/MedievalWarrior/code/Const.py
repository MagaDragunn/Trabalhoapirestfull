# C
import pygame

COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (227, 227, 23)

# M
MENU_OPTION = ( 'NEW GAME KNIGHT',
                'NEW GAME MAGE',
                'NEW GAME ROGUE',
                'SCORE',
                'EXIT')
# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bgr0' : 0,
    'Level1Bgr1' : 1,
    'Level1Bgr2' : 1,
    'Level1Bgr3' : 2,
    'Knight' : 3,
    'Mage' : 1,
    'Rogue' : 5,
    'Enemy1': 1,
    'Enemy2' : 2,
    'Enemy3' : 3
}
# S
SPAWN_TIME = 4000
# W
WIN_WIDTH = 1064
WIN_HEIGHT = 604