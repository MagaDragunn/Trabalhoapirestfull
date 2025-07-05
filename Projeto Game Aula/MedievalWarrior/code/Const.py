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
    'KnightMagic' : 2,
    'Mage' : 1,
    'MageMagic' : 2,
    'Rogue' : 5,
    'RogueMagic' : 2,
    'Enemy1': 1,
    'Enemy2' : 2,
    'Enemy3' : 3
}
ENTITY_HEALTH ={
    'Level1Bgr0': 999,
    'Level1Bgr1': 999,
    'Level1Bgr2': 999,
    'Level1Bgr3': 999,
    'Knight' : 100,
    'Mage' : 80,
    'Rogue' : 70,
    'KnightMagic' : 1,
    'MageMagic' : 1,
    'RogueMagic' : 1,
    'Enemy1': 100,
    'Enemy2' : 200,
    'Enemy3' : 250
}
# P
PLAYER_KEY_LEFT = {'Knight' : pygame.K_LEFT,
                   'Mage' : pygame.K_LEFT,
                   'Rogue' : pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Knight' : pygame.K_RIGHT,
                   'Mage' : pygame.K_RIGHT,
                   'Rogue' : pygame.K_RIGHT}
PLAYER_KEY_MAGIC = {'Knight' : pygame.K_SPACE,
                   'Mage' : pygame.K_SPACE,
                   'Rogue' : pygame.K_SPACE}
# S
SPAWN_TIME = 5000
# W
WIN_WIDTH = 1064
WIN_HEIGHT = 604