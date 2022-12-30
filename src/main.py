import pygame
import os
import random
import math



# pygame init
pygame.init()



# constants and setup
IS_ANDROID = 'ANDROID_ARGUMENT' in os.environ
PATH = "/data/data/ru.harmonica.cataway/files/app/" if IS_ANDROID else "./"
IMAGE_SPIKE = {
    "w": pygame.image.load(PATH+"wspike.png"),
    "b": pygame.image.load(PATH+"bspike.png")}
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
OPCOLORS = {
    'w': "#000000",
    'b': "#ffffff"}
DIRECTION = {
    'w': -1,
    'b': 1
}
DISPLAY_SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DISPLAY_SIZE = DISPLAY_SURFACE.get_size()
FONT = pygame.font.Font(PATH+"font.ttf", 100)
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Cat Away')
pygame.display.set_icon(pygame.image.load(PATH+"icon.png"))



# variables
is_runing = True
selected_color = None
player_position = [0, 0]
spike_positions = []
game_rawscore = 0
game_score = 0

is_alive = True
killer_spike_index = 0


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

        # exit
        if event.type == pygame.QUIT:
            pygame.quit()
            is_runing = False

        # select
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_color = 'b' if event.pos[0] < DISPLAY_SIZE[0] / 2 else 'w'

    pygame.display.update()
            

# game loop
while is_runing:
    # alive loop
    while is_alive:

        CLOCK.tick(60)
        # score increase
        game_score += 1

        # move spikes
        __game_speed = game_score / 100
        __spike_index = 0
        while __spike_index < len(spike_positions):
            spike_positions[__spike_index][0] -= __game_speed
            if math.dist(spike_positions[__spike_index], player_position) <= IMAGE_SIZE[0] / 2:
                is_alive = False
                killer_spike_index = __spike_index

            if spike_positions[__spike_index][0] <= -IMAGE_CENTER[0]:
                del spike_positions[__spike_index]
            else:
                __spike_index += 1

        # create spikes
        __spikes_max = int(DISPLAY_SIZE[1] / IMAGE_SIZE[1] / 2)
        __spike_spawn_speed = math.ceil(game_score / 100 / (len(spike_positions) + 1))
        for __spike_chance in range(random.randint(-__spikes_max + __spike_spawn_speed, __spike_spawn_speed)):
            if __spike_chance > 0:
                spike_positions.append([DISPLAY_SIZE[0] + IMAGE_SIZE[0], random.randint(0, DISPLAY_SIZE[1] - IMAGE_SIZE[1])])

        # background
        DISPLAY_SURFACE.fill(COLORS[selected_color])
        
        # draw player
        if is_alive: DISPLAY_SURFACE.blit(IMAGE_CAT[selected_color], player_position)
        else: DISPLAY_SURFACE.blit(IMAGE_DEAD[selected_color], player_position)

        # draw spikes
        for __spike_position in spike_positions:
            DISPLAY_SURFACE.blit(IMAGE_SPIKE[selected_color], __spike_position)
        
        # draw score
        __score_text = "SCORE:" + str(int(game_score / 10))
        ## shadow
        __score_shadow_surf = FONT.render(__score_text, 0, OPCOLORS[selected_color])
        __score_shadow_tr_surf = __score_shadow_surf.get_rect(topleft=(0, 2))
        __score_shadow_bl_surf = __score_shadow_surf.get_rect(topleft=(2, 0))
        DISPLAY_SURFACE.blit(__score_shadow_surf, __score_shadow_tr_surf)
        DISPLAY_SURFACE.blit(__score_shadow_surf, __score_shadow_bl_surf)
        ## score
        __score_surf = FONT.render(__score_text, 0, COLORS[selected_color])
        __score_rect = __score_surf.get_rect(topleft=(1, 1))
        DISPLAY_SURFACE.blit(__score_surf, __score_rect)

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

        pygame.display.update()

    game_score /= 2
    
    # dead loop
    while not is_alive:
        CLOCK.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                is_runing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                del spike_positions[killer_spike_index]
                is_alive = True

        # dead
        pygame.display.update()
                
