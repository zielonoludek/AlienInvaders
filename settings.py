import pygame

class Settings:
    """wszystkie ustawienia gry"""
    def __init__(self):

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.screen_height = 1000
        self.bg_color = (0,0,0)
        self.text_color = (255, 220, 74)#(255, 246, 137) #(166, 194, 225)

        self.ship_speed = 4
        self. ship_hit= 0

        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 15

        self.alien_speed = 1.5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        self.xp = 10