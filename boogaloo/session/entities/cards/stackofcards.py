from . import CollectionOfCards


class StackOfCards(CollectionOfCards):
    def __init__(self, supported_card_types, refill_from=None):
        super().__init__(supported_card_types)
        self.refill_from = refill_from
