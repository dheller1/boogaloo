from . import InstanceBuilder
from boogaloo.definition.entities.cards import HandDefinition
from boogaloo.session.entities.cards import HandOfCards
from ..definition_reference import Reference


class HandOfCardsBuilder(InstanceBuilder):
    def __init__(self):
        super().__init__(HandDefinition, HandOfCards)

    def _create(self, definition):
        return HandOfCards(owner=None, supported_card_types=definition.supported_card_types,
                           size_limit=definition.size_limit, draw_from=Reference(definition.draw_from))
