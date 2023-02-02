from engine import Application
import pygame
import os



class MyApplication(Application):
    def On_Init(self):
        self.is_android = 'ANDROID_ARGUMENT' in os.environ
        self.path = "/data/data/ru.harmonica.cataway/files/app/" if self.is_android else "./"
        self.images = {
            '0spike':pygame.image.load(os.path.join(self.path, "images", "bspike.png")),
            '1spike':pygame.image.load(os.path.join(self.path, "images", "wspike.png")),
            '0dead': pygame.image.load(os.path.join(self.path, "images", "bdead.png")),
            '1dead': pygame.image.load(os.path.join(self.path, "images", "wdead.png")),
            '0cat':  pygame.image.load(os.path.join(self.path, "images", "bcat.png")),
            '1cat':  pygame.image.load(os.path.join(self.path, "images", "wcat.png")),
        }
        self.colors = {
            0: "#000000",
            1: "#ffffff",
        }
        self.font_7seg = pygame.font.Font(self.path + "7seg.ttf", 100)

        pygame.display.set_caption('Cat Away')
        pygame.display.set_icon(pygame.image.load(os.path.join(self.path, "images", "icon.png")))


        self.selected_color = 0
        self.selected_direction = 1
        



application = MyApplication()