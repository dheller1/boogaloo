from boogaloo.definition.entities.cards import HandDefinition
from boogaloo.session_factory.builders.handofcardsbuilder import HandOfCardsBuilder


class Factory:
    builders = {
        HandDefinition: HandOfCardsBuilder(),
    }

    @staticmethod
    def build_tree(tree_def):
        pass
