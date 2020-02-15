from . import CollectionOfCards


class HandOfCards(CollectionOfCards):
    def __init__(self, owner, supported_card_types, size_limit=None, draw_from=None):
        super().__init__(owner, supported_card_types)
        self.size_limit = size_limit
        self.draw_from = draw_from