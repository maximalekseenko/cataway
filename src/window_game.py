from engine import Window
from application import application
import pygame



class Window_Game(Window):
    def On_Init(self):
        return super().On_Init()

        
    def On_Open(self) -> None:
        self.game_size = (1000, 1000)
        self.cat_size = (100, 100)
        self.is_alife = True
        self.player_position = [
            (self.game_size[0] - self.cat_size[0]) / 2,
            (self.game_size[1] - self.cat_size[1]) / 2,
        ]

        self.Update()


    def On_Close(self) -> None:
        return super().On_Close()


    def On_Handle(self, event: pygame.event.Event) -> None:

        # window resized
        if event.type == pygame.WINDOWSIZECHANGED: self.Update()
        # Move_Cat
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]: self.Move_Cat(*event.rel)
        else: print(event)
    

    def Move_Cat(self, dx, dy):

            # move
            self.player_position[0] += dx / self.scale
            self.player_position[1] += dy / self.scale

            # fix
            # if 0 > self.player_position[0]: self.player_position[0] = 0
            # elif self.player_position[0] > DISPLAY_SIZE[0] - IMAGE_SIZE[0]: self.player_position[0] = DISPLAY_SIZE[0] - IMAGE_SIZE[0]
            # if 0 > self.player_position[1]: self.player_position[1] = 0
            # elif self.player_position[1] > DISPLAY_SIZE[1] - IMAGE_SIZE[1]: self.player_position[1] = DISPLAY_SIZE[1] - IMAGE_SIZE[1]


    def On_Render(self) -> None:
        self._Render_Background()
        self._Render_Cat()
        self._Render_Spikes()
        self._Render_Score()

    
    def _Render_Background(self):
        self.surface.fill(application.colors[application.selected_color])

    
    def _Render_Cat(self):
        self.surface.blit(self.cat_image, (
            self.player_position[0] * self.scale, 
            self.player_position[1] * self.scale,
            self.cat_size[0] * self.scale,
            self.cat_size[1] * self.scale,
            ))


    def _Render_Spikes(self):
        pass

    
    def _Render_Score(self):
        pass


    def On_Update(self):
        __screen_height = application.screen.get_height()
        __screen_width = application.screen.get_width()
        self.scale = __screen_height / 1000

        self.cat_image = pygame.transform.scale(
            application.images[str(application.selected_color) + 'cat'],
            (
                self.cat_size[0] * self.scale,
                self.cat_size[1] * self.scale,
            )
        )


"""

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
                
"""