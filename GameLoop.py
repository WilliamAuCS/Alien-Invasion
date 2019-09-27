import pygame
import Settings
import Ship
import GameFunctions as gf
from pygame.sprite import Group
import GameStats
import Button
import Scoreboard


def run_game():
    # Initialize game loop
    pygame.init()
    ai_settings = Settings.Settings()
    # Create instance to store game statistics and create scoreboard
    stats = GameStats.GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    sb = Scoreboard.Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("Alien Invasion!")

    # Create play button
    play_button = Button.Button(screen, "Play")

    # Make a ship, group of bullets, and group of aliens
    ship = Ship.Ship(ai_settings, screen)
    # Creating bullet group
    bullets = Group()
    aliens = Group()

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    gameRunning = True

    while gameRunning:
        # Responding to key presses and mouse clicks
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            Ship.Ship.update(ship)
            gf.update_bullets(ai_settings, screen, ship, stats, sb, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
