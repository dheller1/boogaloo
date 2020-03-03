import random

from . import CollectionOfCards


class UnsupportedCardTypeException(BaseException):
    pass


class StackOfCards(CollectionOfCards):
    """ An ordered stack of cards. The `cards` collection holds the current stack of cards and is also a stack in
    data-structure sense, i.e. it operates in a last-in first-out fashion: You put cards at the top of the stack and
    also draw them from there. """
    def __init__(self, supported_card_types, cards=None, refill_from=None):
        super().__init__(supported_card_types)
        self.refill_from = refill_from
        self.cards = [] if cards is None else cards

    def draw(self, count=1):
        """ Draws `count` cards from the stack and returns them in the order in which they are drawn
        (i.e. first the top-most card, then the second, etc.) """
        if count > len(self.cards):
            raise IndexError('not enough cards to draw')
        drawn = list(reversed(self.cards[-count:]))
        self.cards = self.cards[:-count]
        return drawn

    def put(self, cards):
        """ Puts the given `cards` on top of the stack. """
        for c in cards:
            if type(c) not in self.supported_card_types:
                raise UnsupportedCardTypeException
            self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)
