import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game, and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # Set the background color
        self.bg_color = (self.settings.bg_color)

    
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit
            
            # Redraw the screen during each pass trough the loop.
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            
            # Make the most recently draw screen visible. 
            # When we move the game elements around display.flip() is gonna update the display to show the new positions of the game and hide old ones.
            pygame.display.flip()

if __name__ == 'main':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

AlienInvasion()


