from boogaloo.definition.entities import GameEntity


class TokenType(GameEntity):
    """ A TokenType instance defines an arbitrary set of tokens with the same meaning. Often all tokens of the same type
    are identical, but they could also refer to different values of the same meaning, e.g. coins with different gold
    values. The token type just defines which and how many variants of a given type of tokens exist, not where they
    are or who owns them.
    Use a TokenCollection for that: Usually, tokens of one type are distributed between various token collections, such
    as game-owned token supplies or player-owned token collections.
    :param multi_values: Can be a list of different values supported by this type of tokens. E.g. [1, 3, 5]
    """
    def __init__(self, multi_values=None):
        super().__init__()
        self.multi_values = multi_values
