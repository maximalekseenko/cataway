import pygame
import os



# pygame init
pygame.init()



# constants and setup
IS_ANDROID = 'ANDROID_ARGUMENT' in os.environ
PATH = "/data/data/org.test.cataway/files/app/" if IS_ANDROID else "./"
IMAGE_SPIKE = {
    "w": pygame.image.load(PATH+"wspike.png"),
    "b": pygame.image.load(PATH+"bspike.png")}
while True:
    pass
IMAGE_DEAD = {
    "w":  pygame.image.load(PATH+"wdead.png"),
    "b":  pygame.image.load(PATH+"bdead.png")}
IMAGE_CAT = {
    "w":   pygame.image.load(PATH+"wcat.png"),
    "b":   pygame.image.load(PATH+"bcat.png")}
IMAGE_SIZE = IMAGE_CAT["b"].get_size()
IMAGE_CENTER = (IMAGE_SIZE[0] / 2, IMAGE_SIZE[1] / 2)
COLORS = {
    'w': "#ffffff",
    'b': "#000000"}
DIRECTION = {
    'w': -1,
    'b': 1
}
DISPLAY_SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DISPLAY_SIZE = DISPLAY_SURFACE.get_size()
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Cat Away')
pygame.display.set_icon(pygame.image.load(PATH+"icon.png"))



# variables
is_runing = True
selected_color = None
player_position = [0, 0]
spike_positions = []
game_score = 0
is_alive = True

is_dragging = False


# select color loop
while is_runing and selected_color == None:
    CLOCK.tick(60)

    # black
    pygame.draw.rect(DISPLAY_SURFACE, COLORS['b'], (
        0, 
        0, 
        DISPLAY_SIZE[0] / 2, 
        DISPLAY_SIZE[1]))

    DISPLAY_SURFACE.blit(IMAGE_CAT['b'], (
        DISPLAY_SIZE[0] * 1 / 4 - IMAGE_CENTER[0], 
        DISPLAY_SIZE[1] * 1 / 2 - IMAGE_CENTER[1]))

    # white
    pygame.draw.rect(DISPLAY_SURFACE, COLORS['w'], (
        DISPLAY_SIZE[0] / 2, 
        0, 
        DISPLAY_SIZE[0] / 2, 
        DISPLAY_SIZE[1]))

    DISPLAY_SURFACE.blit(IMAGE_CAT['w'], (
        DISPLAY_SIZE[0] * 3 / 4 - IMAGE_CENTER[0], 
        DISPLAY_SIZE[1] * 1 / 2 - IMAGE_CENTER[1]))
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            is_runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_color = 'b' if event.pos[0] < DISPLAY_SIZE[0] / 2 else 'w'

    pygame.display.update()
            


# game loop
# select color loop
while is_runing:
    CLOCK.tick(60)

    DISPLAY_SURFACE.fill(COLORS[selected_color])
    
    # player
    if is_alive: DISPLAY_SURFACE.blit(IMAGE_CAT[selected_color], player_position)
    else: DISPLAY_SURFACE.blit(IMAGE_DEAD[selected_color], player_position)

    # spikes
    for _spike_position in spike_positions:
        DISPLAY_SURFACE.blit(IMAGE_SPIKE[selected_color], _spike_position)
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            is_runing = False

        if event.type == pygame.MOUSEMOTION:

            # move
            player_position[0] += event.rel[0]
            player_position[1] += event.rel[1]

            # fix
            if 0 > player_position[0]: player_position[0] = 0
            elif player_position[0] > DISPLAY_SIZE[0] - IMAGE_SIZE[0]: player_position[0] = DISPLAY_SIZE[0] - IMAGE_SIZE[0]
            if 0 > player_position[1]: player_position[1] = 0
            elif player_position[1] > DISPLAY_SIZE[1] - IMAGE_SIZE[1]: player_position[1] = DISPLAY_SIZE[1] - IMAGE_SIZE[1]

            if event.touch == True: selected_color = 'b' if selected_color == 'w' else 'w'

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pass

    pygame.display.update()
            
