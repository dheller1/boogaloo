from boogaloo.entities.cards import CardCollection


class HandOfCards(CardCollection):
    def __init__(self, supported_card_types, size_limit=None, draw_from=None):
        super().__init__(supported_card_types)
        self.size_limit = size_limit
        self.draw_from = draw_from
