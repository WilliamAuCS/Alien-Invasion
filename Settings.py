class Settings:

    def __init__(self):
        """Initializing game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullets_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.ship_limit = 3

        # Speeding the game up
        self.speedup_scale = 1.1

        # How quickly alien score increases based on game level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullets_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Initial score of each alien
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullets_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
