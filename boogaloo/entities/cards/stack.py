from boogaloo.entities.cards import CardCollection


class StackOfCards(CardCollection):
    """ A stack of cards is a collection of cards which are usually placed on top of each other.
    It is often a draw or discard pile, and can be face-up or face-down. """
    def __init__(self, supported_card_types):
        super().__init__(supported_card_types)
