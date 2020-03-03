from boogaloo.core.pickdecision import PickDecision
from . import CollectionOfCards


class HandOfCards(CollectionOfCards):
    def __init__(self, supported_card_types, size_limit=None):
        super().__init__(supported_card_types)
        self.size_limit = size_limit

    def draw_from(self, source, count=1):
        """ Draws `count` cards from the given `source` and adds them to the hand. """
        self.cards.extend(source.draw(count))

    def discard_decision(self, discard_to, count=1):
        """ Generates and returns a Decision which requires to choose `count` cards to discard from the hand. """
        decision = PickDecision(options=self.cards, required_choices=count)
        return decision
