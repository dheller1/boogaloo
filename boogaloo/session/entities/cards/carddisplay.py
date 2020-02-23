from boogaloo.session.entities.cards import CollectionOfCards


class CardDisplay(CollectionOfCards):
    """ A card display is an area in which cards can be placed, face-up or face-down.
    It is both commonly used as a global or a per-player entity, representing cards available to all players,
    or cards under control of a player, respectively. """
    def __init__(self, supported_card_types):
        super().__init__(supported_card_types)
