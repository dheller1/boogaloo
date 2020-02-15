from boogaloo.entities.cards import CardCollection


class StackOfCards(CardCollection):
    """ A stack of cards is a collection of cards which are usually placed on top of each other.
    It is often a draw or discard pile, and can be face-up or face-down.
    :param supported_card_types: list of card types that can be contained
    :param refill_from: a card collection from which the stack is refilled, once its last card was drawn.
    """
    def __init__(self, supported_card_types, refill_from=None):
        super().__init__(supported_card_types)
        self.refills_from = refill_from
