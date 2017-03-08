from settings import config
import pygame

from graphics import draw_table


class Game:
    """
    Container for game elements - components, players - and mechanics
    """
    def __init__(self):
        self.components = None
        self.current_player = None
        self.buttons = None
        self.players = None
        self.mechanics = None

    def init_game(self, players, buttons, components, mechanics):
        self.players = players
        self.components = components
        self.buttons = buttons
        self.mechanics = mechanics

    def embody(self):
        game.buttons.reset()
        draw_table()

        self.components.table_chips.embody()

        self.components.table_card_stacks.embody(
            location=config.central_area_location + config.card_decks_location
        )

        self.components.table_card_grid.embody()

        for tile in self.components.table_tiles.components:
            tile.embody()

        self.components.holding_area.embody()

        # There can only be one card in the holding area -
        # no need to specify a column
        for card in self.components.holding_area_cards:
            card.embody()

        for player in self.players:
            player.embody()

        pygame.display.flip()


    # def embody(self):
    #     """
    #     Embody the game
    #     - Create all available buttons
    #     - Draw the table, holding and player areas
    #     """
    #
    #     # Remove previously created buttons
    #     game.buttons.reset()
    #
    #     draw_table()
    #
    #     game.components.embody()
    #     for player in game.players:
    #         player.embody()
    #     pygame.display.flip()


game = Game()
