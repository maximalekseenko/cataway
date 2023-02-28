from engine import Window
from application import application
import pygame
import random



class Window_Game(Window):
    def On_Init(self):
        return super().On_Init()

        
    def On_Open(self) -> None:
        self._New_Game()
        self.Update()
    

    def _New_Game(self):
        self.seed = random.randint(0, 99999)
        self.score = 0

        self.game_size = (1000, 1000)
        self.cat_size = (100, 100)
        self.spike_size = (100, 100)

        self.is_alive = True
        self.cat_position = [
            (self.game_size[0] - self.cat_size[0]) / 2,
            (self.game_size[1] - self.cat_size[1]) / 2,
        ]


    def On_Close(self) -> None:
        return super().On_Close()


    def On_Handle(self, event: pygame.event.Event) -> None:

        # window resized
        if event.type == pygame.WINDOWSIZECHANGED: self.Update()
        # Move_Cat
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]: self.Move_Cat(*event.rel)
        else: print(event)
    

    def Score(self):
        self.score += application.clock.get_time()
        self.score_delta = application.clock.get_time()


    def Move_Cat(self, dx, dy):

            # move
            self.cat_position[0] += dx / self.scale
            self.cat_position[1] += dy / self.scale

            # fix out of bounds
            if 0 > self.cat_position[0]: self.cat_position[0] = 0
            elif self.cat_position[0] > self.game_size[0] - self.cat_size[0]: self.cat_position[0] = self.game_size[0] - self.cat_size[0]
            if 0 > self.cat_position[1]: self.cat_position[1] = 0
            elif self.cat_position[1] > self.game_size[1] - self.cat_size[1]: self.cat_position[1] = self.game_size[1] - self.cat_size[1]


    def On_Render(self) -> None:
        # TODO Move from render
        self.Score()
        self._Render_Background()
        self._Render_Cat()
        self._Render_Spikes()
        self._Render_Score()
        if application.debug:self._Render_Debug()

    
    def _Render_Background(self):
        # background
        self.surface.fill(application.colors[application.selected_color])
        # wall
        pygame.draw.line(self.surface, 
            application.colors[2], 
            (
                self.game_size[0] * self.scale,
                0,
            ),
            (
                self.game_size[0] * self.scale,
                self.game_size[1] * self.scale,
            )
        )

    
    def _Render_Cat(self):
        self.surface.blit(self.cat_image, (
            self.cat_position[0] * self.scale, 
            self.cat_position[1] * self.scale,
            self.cat_size[0] * self.scale,
            self.cat_size[1] * self.scale,
            ))


    def _Render_Spikes(self):
        pass

    
    def _Render_Score(self):
        pass


    def _Render_Debug(self):
        textlist = {
            'catpos': self.cat_position,
            'score': self.score,
            'scored': self.score_delta,
            'scale': self.scale,
        }
        __text_top = 0
        for __name, __value in textlist.items():
            text_surf = application.font_none.render(f"{__name}:{__value}", 0, "#ffffff", "#000000")
            text_rect = text_surf.get_rect(left=0, top=__text_top)
            self.surface.blit(text_surf, text_rect)
            __text_top += text_rect.height


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
            if math.dist(spike_positions[__spike_index], cat_position) <= IMAGE_SIZE[0] / 2:
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
        if is_alive: DISPLAY_SURFACE.blit(IMAGE_CAT[selected_color], cat_position)
        else: DISPLAY_SURFACE.blit(IMAGE_DEAD[selected_color], cat_position)

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
                cat_position[0] += event.rel[0]
                cat_position[1] += event.rel[1]

                # fix
                if 0 > cat_position[0]: cat_position[0] = 0
                elif cat_position[0] > DISPLAY_SIZE[0] - IMAGE_SIZE[0]: cat_position[0] = DISPLAY_SIZE[0] - IMAGE_SIZE[0]
                if 0 > cat_position[1]: cat_position[1] = 0
                elif cat_position[1] > DISPLAY_SIZE[1] - IMAGE_SIZE[1]: cat_position[1] = DISPLAY_SIZE[1] - IMAGE_SIZE[1]

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