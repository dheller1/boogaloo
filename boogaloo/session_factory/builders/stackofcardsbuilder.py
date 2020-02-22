from . import InstanceBuilder
from boogaloo.definition.entities.cards import StackDefinition
from ..definition_reference import Reference
from ...session.entities.cards.stackofcards import StackOfCards


class StackOfCardsBuilder(InstanceBuilder):
    def __init__(self):
        super().__init__(StackDefinition, StackOfCards)

    def _create(self, definition):
        return StackOfCards(supported_card_types=definition.supported_card_types,
                            refill_from=Reference(definition.refill_from))
