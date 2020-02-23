from . import InstanceBuilder
from boogaloo.definition.entities.tokens import TokenCollectionDefinition
from boogaloo.session.entities.tokens.tokencollection import TokenCollection


class TokenCollectionBuilder(InstanceBuilder):
    def __init__(self):
        super().__init__(TokenCollectionDefinition, TokenCollection)

    def _create(self, definition):
        return TokenCollection(definition.token_type, definition.start_amount, definition.unlimited)
