from boogaloo.definition.entities import EntityDefinition


class TokenCollectionDefinition(EntityDefinition):
    """ A TokenCollectionDefinition is often a global supply of tokens, or the private collection of a single player.
    :param token_type: A TokenType instance defining the type of tokens contained in the supply.
    :param start_amount: The number or total value of tokens initially contained in the supply.
    :param unlimited: If this is true, the supply can never run empty: The 'amount' is purely a virtual/display
    consideration and tokens can always be drawn from it.
    """
    def __init__(self, token_type, start_amount, unlimited=False):
        super().__init__()
        self.token_type = token_type
        self.unlimited = unlimited
        self.start_amount = start_amount
