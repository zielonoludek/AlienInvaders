import pygame.font
from game_stats import Game_stats
from settings import Settings


class Message():

    def __init__(self, game, msg):

        pygame.font.init()
        font = ('Res/couriernew.ttf')

        self.stats = Game_stats(self)
        self.screen = game.screen
        self.settings = Settings()

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(font, 32)

        self.rect = pygame.Rect(20, 0, 400, 45)
        self.rect.center = game.screen.get_rect().midtop

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midtop = self.rect.midbottom

    def draw_button(self):
        self.screen.fill((0,0,0),self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)