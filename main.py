import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Game_stats
from button import Button
from message import Message


class Gra_alieni:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_width = int(self.settings.screen_width)
        self.screen_height = int(self.settings.screen_height)

        pygame.display.set_caption('Aliens')

        self.stats = Game_stats(self)
        self.ship = Ship(self)
        self.alien = Alien(self)
        self.bullets = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        self.points = self.stats.points

        self.create_fleet()

    def run_game(self):

        """main loop"""

        while True:
            self.check_events()

            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_alien()

            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.act_pos()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet(game)
        self.alien_group.draw(self.screen)

        if len(self.alien_group) == 0:
            self.stats.game_active = False

        if not self.stats.game_active:
            if len(self.alien_group) > 0 and self.settings.ship_hit == 0:
                Button(self, 'START').draw_button()
                Message(self, ' Choose difficulty level 1 -> easy, 2 -> mid or 3 ->  hard ').draw_button()

            elif len(self.alien_group) == 0:
                sleep(1)
                Button(self, "You're a winner!").draw_button()
                pygame.mouse.set_visible(True)
                Message(self, f'To play again press ENTER or the button below:').draw_button()

            elif self.settings.ship_hit != 0:
                sleep(1)
                Button(self, 'You lose').draw_button()
                Message(self, f'To play again press ENTER or the button below:').draw_button()
        else:
            Message(self, f'Defeated  {self.stats.points} aliens').draw_button()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_clicked = Button(self, 'Start').rect.collidepoint(mouse_pos)

                if button_clicked and not self.stats.game_active:
                    self.stats.game_active = True
                    self.reset()
                    pygame.mouse.set_visible(False)

    def keydown_events(self, event):

        if event.key == pygame.K_d:
            self.ship.moving_right = True

        elif event.key == pygame.K_a:
            self.ship.moving_left = True

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

        if not self.stats.game_active:
            if event.key == pygame.K_RETURN:
                self.stats.game_active = True
                self.reset()
                pygame.mouse.set_visible(False)

            if event.key == pygame.K_2:
                self.mid()
            if event.key == pygame.K_3:
                self.hard()
            if event.key == pygame.K_1:
                self.easy()
        if event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed and self.stats.game_active:
                self.bullets.add(Bullet(self))

    def reset(self):
        self.alien_group.empty()
        self.bullets.empty()
        self.create_fleet()
        self.ship.__init__(game)
        self.stats.points = 0

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

            pygame.sprite.groupcollide(self.bullets, self.alien_group, True, True)
            self.stats.points = self.stats.a_amount - len(self.alien_group)

    def create_fleet(self):
        number_aliens = (self.screen_width - (2*self.alien.rect.width)) // (2*self.alien.rect.width)
        number_rows = (self.screen_height - self.ship.rect.height - (4*self.alien.rect.height)-2
                       ) // (2*self.alien.rect.height)

        self.stats.a_amount = number_rows*number_aliens
        for rows in range(number_rows):
            for alien_number in range(number_aliens):
                self.create_alien(alien_number, rows)

    def create_alien(self, alien_number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.rect.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        self.alien_group.add(alien)

    def update_alien(self):
        self.check_fleet_edges()
        self.alien_group.update()

        if pygame.sprite.spritecollideany(self.ship, self.alien_group):
            self.settings.ship_hit = 1
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        self.check_allien_bottom()

    def check_fleet_edges(self):
        for alien in self.alien_group.sprites():
            if alien.check_edge():
                for alien in self.alien_group.sprites():
                    alien.rect.y += self.settings.fleet_drop_speed
                self.settings.fleet_direction *= -1
                break

    def check_allien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.alien_group.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.settings.ship_hit = 1
                self.settings.ship_hit = 1
                self.stats.game_active = False
                pygame.mouse.set_visible(True)
                break
    def mid(self):
        self.settings.ship_speed = 6
        self.settings.bullet_speed = 3
        self.settings.bullet_width = 3
        self.settings.alien_speed = 2
        self.settings.xp = 20
        self.settings.bullets_allowed = 5

    def hard(self):
        self.settings.ship_speed = 8
        self.settings.bullet_speed = 5
        self.settings.bullet_width = 3
        self.settings.alien_speed = 2.5
        self.settings.xp = 30
        self.settings.bullets_allowed = 1

    def easy(self):
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 15

while __name__ == '__main__':
    game = Gra_alieni()
    game.run_game()
