import pygame.font
from game_stats import Game_stats
from settings import Settings


class Button():

    def __init__(self, game, msg):

        pygame.font.init()
        font = ('Res/couriernew.ttf')

        self.stats = Game_stats(self)
        self.screen = game.screen
        self.settings = Settings()

        self.button_color = (220, 16, 46)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(font, 48)

        self.rect = pygame.Rect(0,0, 300, 80)
        self.rect.center = game.screen.get_rect().center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
