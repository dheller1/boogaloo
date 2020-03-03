from ..entity import Entity


class CollectionOfCards(Entity):
    """ Base class for any set of cards such as card piles, hands, stacks, and displays containing cards.
    Often, they support drawing cards from them, adding cards to them, shuffling, and other operations.
    """
    def __init__(self, supported_card_types):
        super().__init__()
        self.supported_card_types = supported_card_types
        self.cards = []
