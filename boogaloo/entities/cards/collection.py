from boogaloo.entities import GameEntity


class CardCollection(GameEntity):
    """ Base class for card piles, hands, stacks, and displays containing cards. """
    def __init__(self, supported_card_types):
        super().__init__()
        self.supported_card_types = supported_card_types
