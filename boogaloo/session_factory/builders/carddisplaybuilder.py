from . import InstanceBuilder
from boogaloo.definition.entities.cards import DisplayDefinition
from boogaloo.session.entities.cards.carddisplay import CardDisplay


class CardDisplayBuilder(InstanceBuilder):
    def __init__(self):
        super().__init__(DisplayDefinition, CardDisplay)

    def _create(self, definition):
        return CardDisplay(definition.supported_card_types)
