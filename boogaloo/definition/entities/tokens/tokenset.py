from boogaloo.definition.entities import GameEntity


class TokenSet(GameEntity):
    """ A token set defines an arbitrary set of tokens with the same meaning. Often all tokens in a set are identical,
    but they could also refer to different values of the same meaning, e.g. coins with different gold values.
    The token set just defines which and how many variants of a token type exist, not where they are or who owns them.
    (Use a TokenCollection for that).
    :param multi_values: Can be a list of different values supported by this type of tokens. E.g. [1, 3, 5]
    """
    def __init__(self, multi_values=None):
        super().__init__()
        self.multi_values = multi_values
