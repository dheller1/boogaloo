from boogaloo.entities import GameEntity


class CardCollection(GameEntity):
    """ Base class for card piles, hands, stacks, and displays containing cards.
    Once instantiated, collections of cards act as a container with a specific meaning within that game.
    Often, they support drawing cards from them, adding cards to them, shuffling, and other operations.
    """
    def __init__(self, supported_card_types):
        super().__init__()
        self.supported_card_types = supported_card_types
