# C
import pygame

C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (227, 227, 23)
C_GREEN = (0, 128, 0)

# M
MENU_OPTION = ( 'NEW GAME KNIGHT',
                'NEW GAME MAGE',
                'NEW GAME ROGUE',
                'SCORE',
                'EXIT')
# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bgr0' : 0,
    'Level1Bgr1' : 1,
    'Level1Bgr2' : 1,
    'Level1Bgr3' : 2,
    'Level2Bgr0': 0,
    'Level2Bgr1': 1,
    'Level2Bgr2': 1,
    'Level2Bgr3': 2,
    'Level2Bgr4': 2,
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
    'Level2Bgr0': 999,
    'Level2Bgr1': 999,
    'Level2Bgr2': 999,
    'Level2Bgr3': 999,
    'Level2Bgr4': 999,
    'Knight' : 250,
    'Mage' : 200,
    'Rogue' : 300,
    'KnightMagic' : 1,
    'MageMagic' : 1,
    'RogueMagic' : 1,
    'Enemy1': 100,
    'Enemy2' : 200,
    'Enemy3' : 250
}
# D
ENTITY_DAMAGE = {
    'Level1Bgr0': 0,
    'Level1Bgr1': 0,
    'Level1Bgr2': 0,
    'Level1Bgr3': 0,
    'Level2Bgr0': 0,
    'Level2Bgr1': 0,
    'Level2Bgr2': 0,
    'Level2Bgr3': 0,
    'Level2Bgr4': 0,
    'Knight': 10,
    'Mage': 15,
    'Rogue': 20,
    'KnightMagic': 25,
    'MageMagic': 30,
    'RogueMagic': 45,
    'Enemy1': 2,
    'Enemy2': 4,
    'Enemy3': 6
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
SPAWN_TIME = 100
TIMEOUT_STEP = 1000
TIMEOUT_LEVEL = 50000
# W
WIN_WIDTH = 1064
WIN_HEIGHT = 604